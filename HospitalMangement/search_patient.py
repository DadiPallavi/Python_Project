# search_patient.py

from db_connection import cur_obj

class SearchPatient:

    def search(self, name):

        query = "select * from patients where patient_name=%s"

        cur_obj.execute(query, (name,))
        data = cur_obj.fetchone()

        if data:
            print(data)
        else:
            print("Patient Not Found")