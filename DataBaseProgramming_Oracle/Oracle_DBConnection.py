import cx_Oracle
con = cx_Oracle.connect('scott/tiger@localhost')
if con is not None:
    print("Connection successful.")
    print("Version: ", con.version)
else:
    print("Connect Not Established.")
con.close()
