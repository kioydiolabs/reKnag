# script for importing to mysql to migrate from filesystem based reknag to mysql based


import os
import mysql.connector
import time
folder = "./"
subfolders = [ f.path for f in os.scandir(folder) if f.is_dir() ]

database = mysql.connector.connect(
  host="192.168.1.69",
  user="reknag",
  password="reknagDevPassword",
  database="reknag"
)


for x in subfolders:
    try:
        f = open(f"{x}/index.js", "r")
        fileContents = f.read()

        if "'" in fileContents:
            quotMarkPosition = fileContents.find("'")
        else:
            quotMarkPosition = fileContents.find("\"")

        fileContentsTrimmed = fileContents[quotMarkPosition+1:-2]

        print(fileContents+" --> "+fileContentsTrimmed+" --> "+x[2:])


        mycursor = database.cursor()
        sql = "INSERT INTO reknag.URLs (ShortURL, TargetURL) VALUES (%s, %s)"
        val = (x[2:],fileContentsTrimmed)
        mycursor.execute(sql, val)
        database.commit()
        time.sleep(1)
    except Exception as e:
        print(f"Failed to push entry - Reason : {e}")