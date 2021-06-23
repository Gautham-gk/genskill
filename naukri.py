import requests
import bs4
import json


url = "https://www.naukri.com/jobapi/v3/search?noOfResults=20&urlType=search_by_key_loc&searchType=adv&keyword=python&location=bangalore&k=python&l=bangalore&seoKey=python-jobs-in-bangalore&src=jobsearchDesk&latLong="

headers={"appid" : "109",
         "systemid" : "109"}
r = requests.get(url, headers=headers)
data = r.json()
print(type(data))
jobid = 1
for i in data['jobDetails']:
  #  print (i['title'], i['companyName'])
    for k,v in i.items():
         print("K and v",k,"    ",v)
         break
    soup = bs4.BeautifulSoup(i['jobDescription'],features="lxml")
    f = open("Naukri"+str(jobid)+".txt", "w")
    f.write(i['title'])
    f.write(i['companyName'])
    f.write("\n\n")
    f.write(soup.text)
    f.close()
    jobid += 1


