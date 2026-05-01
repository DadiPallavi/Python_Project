

from db_connection import cur_obj

class Billing:

    def generate_bill(self, patient_name):

        query = """
        select p.patient_name,d.fees
        from patients p, doctors d
        where p.patient_name=%s
        limit 1
        """

        cur_obj.execute(query, (patient_name,))
        data = cur_obj.fetchone()

        if data:
            print("Patient Name :", data[0])
            print("Total Bill :", data[1])
        else:
            print("Record Not Found")