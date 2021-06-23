import requests
import bs4
import json


url = "https://www.naukri.com/python-jobs-in-bangalore-bengaluru?k=python&l=bangalore%2Fbengaluru"
headers={"appid" : "109",
         "systemid" : "109"}
r = requests.get(url, headers=headers)
data = r.json()
jobid = 1
for i in data['jobDetails']:
    print (i['title'], i['companyName'])
    soup = bs4.BeautifulSoup(i['jobDescription'],features="html.parser")
    f = open(str(jobid)+".txt", "w")
    f.write(i['title'])
    f.write(i['companyName'])
    f.write("\n\n")
    f.write(soup.text)
    f.close()
    jobid += 1

