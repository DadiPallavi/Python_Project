print("choose one option below")
print("1.Register")
print("2.login")

i=input("choose one from above features")
if int(i)==1:
    from register import Register
    name_input=input("Enter your Name:")
    acc_num_input=input("Enter yr account number :")
    balance_input=input("enter yr frist balance:--")
    p_input=input("enter your password:")
    c_p_input=input("enter yr password again :")
    Register(name_input,acc_num_input,balance_input,p_input,c_p_input)
elif int(i)==2:
    from login import Login
    ac_number=input("enter ur account number :-- ")
    p_Login=input("enter Login password here:-- ")
    Login(ac_number,p_Login)