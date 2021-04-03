import pymysql

conn = pymysql.connect(host="localhost", user="root", passwd="password123", db='sarjeraodb')
mycursor = conn.cursor()
try:
    mycursor.execute("select * from names where id=101")
    print(mycursor.fetchall())
    print()
    mycursor.execute("select * from names")
    print(mycursor.fetchall())
    conn.commit()
except Exception as e:
    print("Error Occured: ", e)
finally:
    conn.close()