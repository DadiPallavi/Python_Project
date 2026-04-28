import mysql.connector
dbc=mysql.connector.connect(
    host="localhost",
    user="root",
    database="d12oopsproject",
    password="root"

)
tablecreationquery="""
create table if not exists employees(
id int primary key,
name varchar(50) not null,
age int,
email varchar(50) not null unique,
salary decimal(10,2) not null
)
"""
print("database connected sucessfully...")

cursor__=dbc.cursor()
cursor__.execute(tablecreationquery)
while True:
    print("1.add employee")
    print("2.read employee")
    print("3.update employee")
    print("4.delete employee")
    print("5.exist")
    o = int(input("enter the choice here:-- "))
    if o==1:
        i=int(input("enter id here :--"))
        n=input("enter the name here:-- ")
        a=int(input("enter the age here:-- "))
        e=input("enter the email:-- ")
        s=float(input("enter salary here:--"))
        queryinsertingemp="insert into employees (id,name,age,email,salary) values(%s,%s,%s,%s,%s)"
        data=(i,n,a,e,s)
        cursor__.execute(queryinsertingemp,data)
        dbc.commit()
        print("employee added sucessfully")
    elif o==2:
        queryreadingemp="select * from employees"
        cursor__.execute(queryreadingemp)
        data=cursor__.fetchall()
        for i in data:
            print(i[1],i[2],i[3],i[4])
    elif o==3:
        queryreadingemp="select * from employees"
        cursor__.execute(queryreadingemp)
        data=cursor__.fetchall()
        for i in data:
            print(i[0],i[1],i[3],i[4])
        id=int(input("enter emp id to update the details of emp :-- "))
        idTobeUpdated=int(input("enter id here to update:-- "))
        ag=int(input("enter age here :-- "))
        sal=float(input("enter slaary here :--   "))

        queryupdateemp="update employees set salary=%s,age=%s,id=%s where id=%s"
        data=(sal,ag,idTobeUpdated,id)
        cursor__.execute(queryupdateemp,data)
        dbc.commit()
        print("emp updated sucessfully.....")
    elif o==4:
        queryreadingemp="select * from employees"
        cursor__.execute(queryreadingemp)
        data=cursor__.fetchall()
        for i in data:
            print(i[0],i[1],i[2],i[3],i[4])
        print("choose id to delete emp")
        id=int(input("enter the id to be deleted in emp table:-- "))
        querydeleteemp="delete from employees where id =%s"
        data=(id,)
        cursor__.execute(querydeleteemp,date)
        dbc.commit()

        print("emp deleted sucessfully...")

    else:
        break

