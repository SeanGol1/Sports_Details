import requests
import json
import datetime

url = "https://golf-leaderboard-data.p.rapidapi.com/tour-rankings/2/2021"

headers = {
    'x-rapidapi-key': "6e6c8988edmsh9dde74a11f1bfa3p18e7b1jsnab2498895645",
    'x-rapidapi-host': "golf-leaderboard-data.p.rapidapi.com"
    }

#response2 = requests.request("GET", url2, headers=headers)

request = requests.get(url, headers=headers)
dict = request.json()
count = 0
leaderboard = []
leaders = ''

dict1= dict.get('results')   
for i in dict1.get('rankings'):
    if count < 10:
        name = i['player_name']
        position = i['position']
        leaderboard.append(name)
        leaders += 'Position '+str(position)+':\n'+name+'\n' 
        count += 1 
    else:
        break
 
        

#print (leaderboard)   #for raspberry pi
print (leaders)       # for laptop


