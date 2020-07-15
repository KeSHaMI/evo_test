/*
    KEY COMPONENTS:
    "activeItem" = null until an edit button is clicked. Will contain object of item we are editing
    "list_snapshot" = Will contain previous state of list. Used for removing extra rows on list update

    PROCESS:
    1 - Fetch Data and build rows "buildList()"
    2 - Create Item on form submit
    3 - Edit Item click - Prefill form and change submit URL
    4 - Delete Item - Send item id to delete URL
    5 - Cross out completed task - Event handle updated item

    NOTES:
    -- Add event handlers to "edit", "delete", "title"
    -- Render with strike through items completed
    -- Remove extra data on re-render
    -- CSRF Token
*/

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

var activeItem = null
var list_snapshot = []

buildList()



function buildList(){
    var wrapper = document.getElementById('list-wrapper')


    var url = 'https://keshami.pythonanywhere.com/api/get_all/'

    fetch(url)
    .then((resp) => resp.json())
    .then(function(data){
        console.log('Data:', data)

        var list = data
        for (var i in list){


            try{
                document.getElementById(`data-row-${i}`).remove()
            }catch(err){

            }


            var death_time = new Date(list[i].death_time)
            death_time = `${death_time.getHours()}:${death_time.getMinutes()}:${death_time.getSeconds()}`
            var name = `<span class="title">${list[i].name}</span>`
            var item = `
                <div id="data-row-${i}" class="task-wrapper flex-wrapper">
                    <div style="flex:7">
                        ${name}
                    </div>
                    <div style="flex:10">
             
                        <small id="death-${i}">Death time: ${death_time}</small>
                             
                    </div>
                    <div style="flex:1">
                        <a href="https://keshami.pythonanywhere.com/api/get/${list[i].id}">Download</a>     
                    </div>
                     
                </div>
                `


            wrapper.innerHTML += item

        }

        if (list_snapshot.length > list.length){
            for (var i = list.length; i < list_snapshot.length; i++){
                document.getElementById('data-row-${i}').remove()
            }
        }

        list_snapshot = list



    })


}


var form = document.getElementById('form-wrapper')
form.addEventListener('submit', function(e){
    e.preventDefault()
    console.log('Form submitted')
    var url = 'https://keshami.pythonanywhere.com/api/create/'

    var title = document.getElementById('title').value
    var death_time = document.getElementById('settime').value.split(':')
    var kyiv_time = Date().toLocaleString('en-US', {timeZone: 'Europe/Kiev'})

    var date = new Date(kyiv_time)
    console.log(date)
    date.setHours(death_time[0])
    date.setMinutes(death_time[1])
    date.setSeconds(death_time[2])
    console.log(date)

    var file = document.getElementById('file')

    var formdata = new FormData()
    formdata.append('file', file.files[0])
    formdata.append('name', title)
    formdata.append('death_time',date.toISOString())
    console.log(formdata.getAll('file'))
    console.log(date)
    console.log(title)
    console.log(file.files[0])
    fetch(url, {
        method:'POST',
        headers:{

            'X-CSRFToken':csrftoken,
        },
        body: formdata}
        ).then(function(response){
        if (response.status === 403){
            alert('Invalid time!')
        }
        buildList()
        document.getElementById('form').reset()
    })
})




