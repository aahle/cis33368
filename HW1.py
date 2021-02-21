
import mysql.connector
from mysql.connector import Error

mydb= mysql.connector.connect(host="localhost", user="ahle20", passwd="RzG6g2/@Ra*", database="testdatabase")

mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE testdatabase")

#mycursor.execute("CREATE TABLE person (name VARCHAR(20), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")

mycursor.execute("INSERT INTO person (name, age) VALUES (%s,%s)", ("Dianna",32))
mydb.commit()

mycursor.execute(" SELECT * FROM person")

for x in mycursor:
    print(x)
