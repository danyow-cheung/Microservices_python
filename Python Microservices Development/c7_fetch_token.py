import requests

TOKENDEALER_SERVER = "http://localhost:5000"
SECRET = "f0fdeb1f1584fd5431c4250b2e859457"

def get_token():
    data = {
        'client_id':'worker1',
        'client_secret':SECRET,
        'audience':'jeeves.domain',
        'grant_type':'client_credentitals',
    }
    headers = {'Content-Type':'application/x-www-form-urlencoded'}
    url = TOKENDEALER_SERVER+'/oauth/token'
    response = requests.post(url,data=data,headers=headers)
    return response.json()['access_token']

