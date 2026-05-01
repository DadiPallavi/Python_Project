

from patient import Patient
from login import Login
from doctor import Doctor
from appointment import Appointment
from admit_discharge import AdmitDischarge
from billing import Billing
from search_patient import SearchPatient

p = Patient()
l = Login()
d = Doctor()
a = Appointment()
ad = AdmitDischarge()
b = Billing()
s = SearchPatient()

while True:

    print("\n1.Register Patient")
    print("2.Patient Login")
    print("3.Doctor Details")
    print("4.Appointment Booking")
    print("5.Admit Patient")
    print("6.Discharge Patient")
    print("7.Bill Generation")
    print("8.Search Patient")
    print("9.Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:
        p.register_patient(
            input("Name: "),
            int(input("Age: ")),
            input("Gender: "),
            input("Mobile: "),
            input("Problem: "),
            input("Visit Type: ")
        )

    elif ch == 2:
        l.patient_login(
            input("Name: "),
            input("Mobile: ")
        )

    elif ch == 3:
        d.add_doctor(
            input("Doctor Name: "),
            input("Specialization: "),
            int(input("Fees: "))
        )

    elif ch == 4:
        a.book_appointment(
            input("Patient Name: "),
            input("Doctor Name: "),
            input("Date: "),
            input("Time: ")
        )

    elif ch == 5:
        ad.admit_patient(input("Patient Name: "))

    elif ch == 6:
        ad.discharge_patient(input("Patient Name: "))

    elif ch == 7:
        b.generate_bill(input("Patient Name: "))

    elif ch == 8:
        s.search(input("Patient Name: "))

    elif ch == 9:
        break