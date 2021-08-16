import requests
import json

from user import *
from store import *



for usr in user:
    u = requests.post('http://localhost:3000/auth/register', usr)    
for str in store:
    s = requests.post('http://localhost:3000/store/register', str)  




print(u.status_code)
print(u.content)


print(s.status_code)
print(s.content)




