import requests
import os
import random
import string

#Character list for password creation and a random seed to initialize the number generation
chars = string.ascii_letters + string.digits + '!@#%^&()'
random.seed = (os.urandom(1024))

#random email provider generator
emails= ['@gmail.com','@yahoo.com','@hotmail.com','@outlook.com','']
characs=['.','_','']

#url containing phsing site
url = 'http://tengbdata.xyz/'


def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

#opening text file containing a list of names
with open("lnames.txt") as f:
    numedefamilie = f.readlines()

numedefamilie = [x.strip() for x in numedefamilie]

with open("lnames.txt") as f:
    prenume = f.readlines()

prenume = [x.strip() for x in prenume]

while True:
    numef_n = random.choice(numedefamilie)
    prenume_n = random.choice(prenume)

    username = numef_n +random.choice(characs) + prenume_n
    username = username.lower() + random.choice(emails)


    password = ''.join(random.choice(chars) for i in range(8))
    
    #change the request data as required
    r=requests.post(url, allow_redirects = False, data = {'Email': username,'contact': password})
    
    #printing the status of every loop and the request
    print ('sending username: %s and password: %s' % (username, password))
    print("POST Request made.")
    print(r.status_code, r.reason)
    print("\n")