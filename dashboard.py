class Dashboard:
    def __init__(self,i):
        print(f"welcome to dashboard {i[1]}")
        print("choose below features to experience our bank")
        print("1.withdraw")
        print("2.depoist")
        print("3.check_balance")
        print("4.logout")
        o=input("choose one from above features")
        if int(o)==1:
            def withdraw(p,iamt):
                nonlocal i
                if p==i[len(i)-1]:
                    if iamt<0:
                        print("enter the valid amount")
                    else:
                        if iamt<i[len(i)-2]:
                            i=list(i)
                            i[len(i)-2]-=iamt
                            print("Remaining amount",i[len(i)-2])
                            q="update users set balance=%s where account_number=%s and password=%s"
                            d=(i[len(i)-2],i[2],i[len(i)-1])
                            from db_connection import cur_obj,db_con_obj
                            cur_obj.execute(q,d)
                            db_con_obj.commit()
                            print("amount update Sucessfully....")
                        else:
                            print("insufficient funds")
                else:
                    print("invalid Validation")
            withdraw(input("enter the password here to withdraw the amount:-- "),int(input("enter the amount u want to withdraw:--")))
        elif int(o)==2:
            def deposits(p,damt):
                nonlocal i
                if p==i[len(i)-1]:
                    if damt>0:
                        i=list(i)
                        i[len(i)-2]+=damt
                        q="update users set balance = %s where account_number=%s and password=%s"
                        d=(i[len(i)-2],i[2],i[len(i)-1])
                        from db_connection import cur_obj,db_con_obj
                        cur_obj.execute(q,d)
                        db_con_obj.commit()
                        print("amount updated Sucessfully as crediting.....")
                        print(f"amount after deposit {i[len(i)-2]}")
            deposits(input("enter password here to deposit the amt:--"),int(input("enter deposit amount here:--")))
        elif int(o)==3:
            def check_bal(password_check_bal):
                if password_check_bal==i[len(i)-1]:
                    print(i[len(i)-2])
                else:
                    print("validation not done")
            check_bal(input("enter password to check the bal"))
        else:
            pass


