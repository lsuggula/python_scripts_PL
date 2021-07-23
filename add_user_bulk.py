import os
import json
import requests
import argparse
import time
from requests.auth import HTTPBasicAuth

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1
    print('======= end-of-3-sec-timer =======') 

PLANET_API_KEY = '123456'
#insert your planet api key

email_list = "abc@stanford.edu;def@stanford.edu;ghi@stanford.edu;jkl@stanford.edu;mno@stanford.edu;pqr@stanford.edu;stu@stanford.edu;vwx@stanford.edu;yz@stanford.edu"

print ("******* email *******")
email = email_list.split(';')
print(email)
print("******* end email *******")

for each_email in email:
  print(each_email)
  payload = {
   "email": each_email,
   "role_level": 100,
   "redirect": "invite/to/#signup"
   #signup page URL where server hits new customer signup
  }
  print ("******* payload *******")
  print (payload)
  admin_url = 'org/level/invite'
  #internal/customer invite button URL in admin-ng page
  print ("******* admin url *******")
  print (admin_url)
  send_invite = requests.post(admin_url, auth=HTTPBasicAuth(PLANET_API_KEY, ''), json=payload)
  sent_invite = send_invite.json()
  print ("******* response returned *******")
  print(json.dumps(sent_invite, indent=1))
  print('-----------------------------------')
  countdown(3)
