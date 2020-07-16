import requests
import datetime
id = 50 ##id need to be relevant
url = 'http://evo-test-pasha.heroku.com/api/'


def test_create():
    URL = url + 'create/'

    client = requests.session()

    client.get(URL)  # sets cookie
    if 'csrftoken' in client.cookies:

        csrftoken = client.cookies.get('csrftoken')
    else:
        # older versions
        csrftoken = client.cookies.get('csrf')

    login_data = dict(name='1', csrfmiddlewaretoken=csrftoken,
                      death_time=datetime.datetime.now() + datetime.timedelta(seconds=5))

    files = {'file': open('dummy', 'rb')}
    print(datetime.datetime.now() + datetime.timedelta(seconds=5))

    r = client.post(URL, data=login_data, headers=dict(Referer=URL), files=files)

    assert r.status_code == 200



def test_get():
    URL = url + 'get/' + str(id)

    client = requests.session()

    r = client.get(URL)

    assert r.status_code == 200


