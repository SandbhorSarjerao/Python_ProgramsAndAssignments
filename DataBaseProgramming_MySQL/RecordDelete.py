import mysql.connector

try:
    conn = mysql.connector.connect(host="localhost", user="root", passwd="password123", db='sarjeraodb')
    mycursor = conn.cursor()
    mycursor.execute("delete from names where id=103")
    print('Record Deleted Successfully.')
    conn.commit()
except Exception as e:
    print("Error Occured: ",e)
finally:
    conn.close()