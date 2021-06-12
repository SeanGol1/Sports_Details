import requests
import json
import datetime
#from datetime import datetime

upcoming = ''
upcoming_list = []
now = datetime.datetime.now()
count = 0


url = "https://golf-leaderboard-data.p.rapidapi.com/fixtures/2/2021"

headers = {
    'x-rapidapi-key': "6e6c8988edmsh9dde74a11f1bfa3p18e7b1jsnab2498895645",
    'x-rapidapi-host': "golf-leaderboard-data.p.rapidapi.com"
    }

#response = requests.request("GET", url, headers=headers)

request = requests.get(url, headers=headers)
json = request.json()
#json = list(json)

for i in json.get('results'):
    if count >= 3:
        break
    name = i["name"]
    course = i["course"]
    country = i["country"]
    starting = i["start_date"]
    ending = i["end_date"]
    prize = i["prize_fund"]
    datecheck = [now.year, now.month, now.day] 
    datecheck2 = starting.split(' ')
    datecheck2.pop(1)
    datecheck2 = datecheck2[0].split('-')
    starting1 = datetime.datetime(int(datecheck2[0]), int(datecheck2[1]), int(datecheck2[2]))
    now1 = datetime.datetime(int(datecheck[0]), int(datecheck[1]), int(datecheck[2]))
    comp = 1
   
    if starting1 < now1:
        continue
      
    else:
        upcoming += 'Upcoming Golf Tournaments\n' 'Name: '+name+ '\nCountry: '+country+ '\nStarting on: '+starting+ '\nPrize money: '+prize+'\n'
        upcoming_list.append(name)
    count += 1 

print (upcoming)        #for laoptop
print (upcoming_list)   #for raspberry pi










    

#print(response.text)

#print(response2.text)