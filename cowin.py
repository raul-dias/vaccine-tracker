#url=("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=151&date=01-05-2021")



import requests as r
from datetime import date

center = '"name":'
age = '"min_age_limit":'
avaliable = '"available_capacity":0'

def getURL( districtCode ):
    d = date.today()
    d1 = d.strftime("%d-%m-%Y")
    url = ("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=")
    url = url + str(districtCode) + "&date=" + str(d1)
    return url

url = getURL(151)
rawdata = r.get(url)
data = rawdata.text
pydata=data.split(",")
count=0
count2=0
for i in pydata:
    if center in i or age in i or avaliable in i:
        count2=count2+1
    else :
        pydata.remove(i)
    count=count+1
print(count)
print(count2)

