class Register:
    def __init__(self,n,ac_num,b,p,c_p):
        from db_connection import cur_obj
        queryCreatingTable= """
        create table if not exists users(
        customer_id int primary key auto_increment,
        name varchar(50) not null unique,
        account_number varchar(20) not null unique,
        balance decimal(10,2) not null,
        password varchar(16) not null
        )
        """
        cur_obj.execute(queryCreatingTable)
        print("table created.....")
        if p==c_p:
            q="insert into users(name,account_number,balance,password) values (%s,%s,%s,%s)"
            d=(n,ac_num,b,p)
            cur_obj.execute(q,d)
            from db_connection import db_con_obj
            db_con_obj.commit()
            print("user register sucessfully...")
            if True:
                from login import Login
                ac_num_login=input("enter yr account number:-- ")
                p_login=input("enter login password here:-- ")
                Login(ac_num_login,p_login)
        else:
            print("password and conform password is not matched")