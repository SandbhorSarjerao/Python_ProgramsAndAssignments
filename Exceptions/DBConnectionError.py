import mysql.connector

try:
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="password123")

    print(mydb)

    if mydb:
        print('Connection Successful')
    else:
        print('Connection UnSuccessful')
except ConnectionError as e:
    print(e)
finally:
    print('Bye...')