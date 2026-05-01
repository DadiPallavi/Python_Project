# patient.py

from db_connection import con_obj, cur_obj
from login import Login

class Patient:

    def __init__(self):

        query = """
        create table if not exists patients(
            patient_id int primary key auto_increment,
            patient_name varchar(50) unique not null,
            patient_age int not null,
            gender varchar(10),
            mobile varchar(10),
            problem varchar(100),
            visit_type varchar(20)
        )
        """

        cur_obj.execute(query)
        con_obj.commit()

    def register_patient(self, name, age, gender, mobile, problem, visit_type):

        queryCheck = "select * from patients where patient_name=%s"
        cur_obj.execute(queryCheck, (name,))
        data = cur_obj.fetchone()

        if data:
            print("Patient Already Registered")
            print("Please Login")

            lg = Login()
            lg.patient_login(
                input("Enter Name: "),
                input("Enter Mobile: ")
            )

        else:
            queryInsert = """
            insert into patients
            (patient_name, patient_age, gender, mobile, problem, visit_type)
            values(%s,%s,%s,%s,%s,%s)
            """

            values = (name, age, gender, mobile, problem, visit_type)

            cur_obj.execute(queryInsert, values)
            con_obj.commit()

            print("Patient Registered Successfully")