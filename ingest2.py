import csv
import psycopg2
dbconn=psycopg2.connect("dbname=superhero")
cursor=dbconn.cursor()	
with open("heroes.csv","r") as file:
	hero=file.readlines()
	print(hero[0])
	for h  in hero:
		h=h.strip()
		list1=h.split(",")
		print(list1[0],list1[1])
		cursor.execute("Insert into character (name,gender) values (%s,%s)",(list1[0],list1[1]))
	dbconn.commit()
  

