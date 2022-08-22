import pymssql

conn = pymssql.connect(server='designdb.database.windows.net', 
                user='designdb-admin@designdb', 
                password='Design2022', 
                database='RawData')

cursor = conn.cursor() 
cursor.execute("INSERT INTO RawData (ServerTimestamp, PositionDirection, PositionLatitude,PositionLongitude,PositionSpeed) VALUES ('12334', '23', '50', '45', '23');")

conn.commit()
print(conn)
