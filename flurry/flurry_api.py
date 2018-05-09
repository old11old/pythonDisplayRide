import requests
import json
import uuid

auth_url = 'https://auth.flurry.com/auth/v1/session'
login_url = 'https://login.flurry.com'
auth_method = 'application/vnd.api+json'

uuID=str(uuid.uuid4())
data = {"data":
            {"type": "session",
             "id": uuID,
             "attributes":{"scopes":"",
                           "email": "flurry@displayride.com",
                           "password": "displayflurry246",
                           "remember": "false"}
             }}


headers1 = {
    'Origin': 'https://login.flurry.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'Content-Type': 'application/vnd.api+json',
    'Accept': 'application/vnd.api+json',
    'Connection': 'keep-alive',
}


with requests.session() as api:
    response = api.options(auth_url , data='')
    headers = response.headers
    for k,v in headers.items():
        print(k,v)
    headers.update({
    'Origin': 'https://login.flurry.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'Content-Type': 'application/vnd.api+json',
    'Accept': 'application/vnd.api+json',
    'Connection': 'keep-alive',
    })
    for k,v in headers.items():
        print(k,v)

    response = api.post(auth_url, data=json.dumps(data), headers=headers)

    print(response)
    print('\n =============')
    if response.status_code == 201:
        for i,k in response.headers.items():
            print(k,': ',v)
        body=response.json()
        print('____________________')
        for i,k in body.items():
            print(k,': ',v)


