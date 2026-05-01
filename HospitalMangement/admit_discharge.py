

from db_connection import con_obj, cur_obj

class AdmitDischarge:

    def admit_patient(self, name):

        query = """
        update patients
        set visit_type='Admitted'
        where patient_name=%s
        """

        cur_obj.execute(query, (name,))
        con_obj.commit()

        print("Patient Admitted")

    def discharge_patient(self, name):

        query = """
        update patients
        set visit_type='Discharged'
        where patient_name=%s
        """

        cur_obj.execute(query, (name,))
        con_obj.commit()

        print("Patient Discharged")