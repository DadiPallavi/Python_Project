                            Hospital Management System Documentation
Project Title:-- Hospital Management System using Python + MySQL


Project Overview:-- The Hospital Management System is a console-based application developed using Python and MySQL.
It is designed to manage hospital operations such as patient registration, login, doctor management, appointment booking, admission/discharge, billing, and patient search.
This project uses Object Oriented Programming (OOP) concepts and modular programming.


Technologies Used:--
Python
MySQL
MySQL Connector (Python Library)
OOP Concepts
Git & GitHub

Project Modules:--
admit_discharge
appointment
billng
dbConnection
doctor details
login
patient register
main
search_patient


File Structure
HospitalManagement/
│── main.py
│── db_connection.py
│── patient.py
│── login.py
│── doctor.py
│── appointment.py
│── admit_discharge.py
│── billing.py
│── search_patient.py


db_connection.py
Purpose:
This module is used to connect Python with MySQL database.

Functionality:
Establishes connection with MySQL server.

Creates cursor object.

Used by all modules for executing SQL queries.

Variables:
con_obj → database connection object

cur_obj → cursor object

patient.py
Purpose:
Handles patient registration.

Features:
Creates patients table if not exists.

Registers new patients.

Checks whether patient already exists.

If already registered, redirects to login.

After new registration, redirects to login.

Table Used:
patients

Important Methods:
__init__() → create table

register_patient() → insert patient details


login.py
Purpose:
Allows patient login.

Features:
Verifies patient name and mobile number.

If login successful:

Welcomes patient

Redirects to appointment booking

Important Methods:
patient_login()



doctor.py
Purpose:
Stores doctor information.

Features:
Creates doctors table.

Adds doctor details.

Displays available doctors.

Table Used:
doctors

Important Methods:
__init__() → create table

add_doctor()

show_doctors()


appointment.py
Purpose:
Books appointments between patient and doctor.

Features:
Creates appointments table.

Shows available doctors.

Books appointment after login.

Table Used:
appointments

Important Methods:
__init__()

show_doctors()

book_appointment()



admit_discharge.py
Purpose:
Manages admission and discharge of patients.

Features:
Admit patient

Discharge patient

Important Methods:
admit_patient()

discharge_patient()


billing.py
Purpose:
Generates patient bill.

Features:
Fetches doctor fee.

Displays total bill.

Important Methods:
generate_bill()


search_patient.py
Purpose:
Search patient details.

Features:
Search patient using patient name.

Shows full patient record.

Important Methods:
search()


main.py:---
Purpose:
Main entry point of project.

Features:
Displays menu-driven program:

Register Patient

Login

Doctor Details

Appointment Booking

Admit Patient

Discharge Patient

Bill Generation

Search Patient

Exit


Database Tables
patients
Stores patient details:

patient_id

patient_name

patient_age

gender

mobile

problem

visit_type


doctors
Stores doctor details:

doctor_id

doctor_name

specialization

fees

appointments
Stores appointment details:

appointment_id

patient_name

doctor_name

appointment_date

timing


OOP Concepts Used
Class
Used to create modules:

Patient

Login

Doctor

Appointment

Billing

Object
Objects created in main.py

Encapsulation
Methods grouped inside classes.

Modular Programming
Each functionality in separate file.


Advantages of Project
Easy to use

Reduces manual work

Fast patient management

Appointment automation

Better hospital data handling

Future Enhancements
GUI using Tkinter

Email/SMS alerts

Admin login

PDF bill generation

Reports dashboard


Conclusion
The Hospital Management System successfully automates hospital operations such as patient registration, doctor management, appointments, billing, and search functions using Python and MySQL.

This project demonstrates real-time database connectivity and OOP concepts.

