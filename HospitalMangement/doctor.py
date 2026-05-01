

from db_connection import con_obj, cur_obj

class Doctor:

    def __init__(self):

        query = """
        create table if not exists doctors(
            doctor_id int primary key auto_increment,
            doctor_name varchar(50),
            specialization varchar(50),
            fees int
        )
        """
        cur_obj.execute(query)
        con_obj.commit()

    def add_doctor(self, name, specialization, fees):

        queryInsert = """
        insert into doctors(doctor_name,specialization,fees)
        values(%s,%s,%s)
        """
        cur_obj.execute(queryInsert, (name, specialization, fees))
        con_obj.commit()

        print("Doctor Added Successfully")

    def show_doctors(self):

        query = "select * from doctors"
        cur_obj.execute(query)

        data = cur_obj.fetchall()

        for i in data:
            print(i)