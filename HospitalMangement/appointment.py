

from db_connection import con_obj, cur_obj

class Appointment:

    def __init__(self):

        query = """
        create table if not exists appointments(
            appointment_id int primary key auto_increment,
            patient_name varchar(50),
            doctor_name varchar(50),
            appointment_date varchar(20),
            timing varchar(20)
        )
        """
        cur_obj.execute(query)
        con_obj.commit()

    def book_appointment(self, pname, dname, date, time):

        queryInsert = """
        insert into appointments
        (patient_name,doctor_name,appointment_date,timing)
        values(%s,%s,%s,%s)
        """

        cur_obj.execute(queryInsert, (pname, dname, date, time))
        con_obj.commit()

        print("Appointment Booked Successfully")