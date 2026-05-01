# login.py

from db_connection import cur_obj

class Login:

    def patient_login(self, name, mobile):

        queryLogin = """
        select * from patients
        where patient_name=%s and mobile=%s
        """

        values = (name, mobile)

        cur_obj.execute(queryLogin, values)
        data = cur_obj.fetchone()

        if data:
            print("Login Successful")
            print("Welcome :", data[1])
            print("Problem :", data[5])
            print("Visit Type :", data[6])
        else:
            print("Invalid Name or Mobile")