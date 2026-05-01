import mysql.connector
con_obj=mysql.connector.connect(
    host="localhost",
    user="root",
    database="cse",
    password="root"
)
cur_obj=con_obj.cursor()
print("db connected sucessfully")