from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import FileSerializer
from .models import File
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.shortcuts import render
from .tasks import delete_file
from django.http import FileResponse, HttpResponseNotFound

# Create your views here.



@api_view(['GET'])
def get_all(request):
    files = File.objects.all().order_by('-id')

    serializer = FileSerializer(files, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def get(request, pk):
    try:
        file = get_object_or_404(File, pk=pk)
    except Http404:
        return render(request, 'api/404.html')
    resp = open(file.file.path, 'rb')
    return FileResponse(resp)
 
@api_view(['POST'])
def create(request):

    serializer = FileSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        file = File.objects.get(pk=serializer.data['id'])

        time = (file.death_time - file.date_created).seconds
        print(time)
        if time > 10000:
            delete_file.delay(time=1, file=serializer.data)
            return Response('time too long', status=403)


        delete_file.delay(time=time, file=serializer.data)

        return Response(serializer.data)

    else:
        return Response(serializer.error_messages, status=400)

