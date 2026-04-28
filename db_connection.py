import mysql.connector

db_con_obj = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="d12oopsproject",
)
cur_obj=db_con_obj.cursor()
print("Connected Successfully")