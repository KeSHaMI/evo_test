from django.http import FileResponse
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .tasks import delete_file
from .models import File
from .serializers import FileSerializer


@api_view(['GET'])
def get_all(request):

    """View which gives all files currently on the server"""
    files = File.objects.all().order_by('-id')

    serializer = FileSerializer(files, many=True)

    return Response(serializer.data)



def get(request, pk):

    """Function for sending file when download clicked"""
    try:
        file = get_object_or_404(File, pk=pk)
    except Http404:
        return render(request, 'api/404.html')

    resp = open(file.file.path, 'rb')

    return FileResponse(resp)

 
@api_view(['POST'])
def create(request):

    """Creating File model and launching delete function"""
    serializer = FileSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        file = File.objects.get(pk=serializer.data['id'])

        time = (file.death_time - file.date_created).seconds
        # if time is less then current timedelta will be huge e.g. 86754 seconds
        if time > 10000:
            #Deleting file if time invalid
            """Of course it's better to not upload file if time invalid, but serializer don't have date_created
             and death_time cannot fit datetime.now(), so to avoid some issues I'm making it like this)"""
            delete_file.delay(time=1, file=serializer.data)
            return Response('time too long', status=403)

        delete_file.delay(time=time, file=serializer.data)

        return Response(serializer.data)

    else:
        return Response(serializer.error_messages, status=400)


def get_view(request, pk):

    """Sending model's info and rendering template"""
    try:
        file = get_object_or_404(File, pk=pk)
    except Http404:
        return render(request, 'api/404.html')

    context = {'death_time': file.death_time,
               'id': file.id,
               'name': file.name}


    return render(request, 'api/file_view.html', context=context)


