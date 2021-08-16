from product import *
import requests
import json
store_auth = {
    
    "email": "eletronica@gmail.com",
    "password": "123",
}    
r = requests.post('http://localhost:3000/store/authenticate',data=store_auth)
print(json.loads(r.text)["token"])

for pd in products:
    p = requests.post('http://localhost:3000/products/register', data= pd,headers={"Authentication":"Bearer " + json.loads(r.text)["token"]})  