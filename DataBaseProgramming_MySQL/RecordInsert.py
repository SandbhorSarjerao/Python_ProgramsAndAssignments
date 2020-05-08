import mysql.connector
conn = mysql.connector.connect(host="localhost", user="root", passwd="password123", db='sarjeraodb')
mycursor = conn.cursor()
mycursor.execute("insert into names values(101,'Sarjerao'),(102,'Navin'),(103,'Priya')")
conn.commit()
conn.close()