import mysql.connector
conn = mysql.connector.connect(host="localhost", user="root", passwd="password123", db='sarjeraodb')
mycursor = conn.cursor()
mycursor.execute("Create table names(id int primary key, name varchar(20))")
conn.commit()
conn.close()