
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345",  
  database="naashik"    
)

my_cursor = mydb.cursor()
my_cursor.execute("SELECT * FROM room")
results=my_cursor.fetchall()
for row in results:
    print(row)
my_cursor.close()
mydb.close()
            
