import pymysql

conn = pymysql.connect(host="localhost", user="root", passwd="password123", db='sarjeraodb')
mycursor = conn.cursor()
try:
    query = 'select * from names'
    mycursor.execute(query)
    print(mycursor.fetchone())
    print()
except Exception as e:
    print("Error Occured: ", e)
finally:
    conn.close()