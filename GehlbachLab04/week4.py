"""
Driver file for medical.py, takes user input and makes calls to medical.py

Author: Abigail Gehlbach
Class: CSI-260-01
Assignment: Week 4 Lab
Due Date: February 13, 2019 11:59 PM

Certification of Authenticity:
I certify that this is entirely my own work, except where I have given
fully-documented references to the work of others. I understand the definition
and consequences of plagiarism and acknowledge that the assessor of this
assignment may, for the purpose of assessing this assignment:
- Reproduce this assignment and provide a copy to another member of academic
- staff; and/or Communicate a copy of this assignment to a plagiarism checking
- service (which may then retain a copy of this assignment on its database for
- the purpose of future plagiarism checking)
"""

import medical

medical.initialize_data()

def get_choice():
    """get user input, no data cleaning"""
    return input("1. Look up a patient by ID number.\n"
                 "2. Add a new patient\n"
                 "3. Quit\n"
                 "Please enter your choice: ")


def create_patient():
    """creates new patient"""
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    address = input("Enter address: ")
    phone_number = input("Enter phone number: ")
    emergency_contact_name = input("Enter emergency contact name: ")
    emergency_contact_num = input("Enter emergency contact number: ")
    
    new_patient = medical.Patient(first_name, last_name, address, phone_number, emergency_contact_name, emergency_contact_num)
    print(f"New patient added with ID {new_patient._id}")


def modify_patient(patient):
    """allows user to modify patient"""
    choice = input("a. Change patient name\n"
                   "b. Change patient address\n"
                   "c. Change patient phone\n"
                   "d. Change emergency contact name\n"
                   "e. Change emergency contact number\n"
                   "Input choice: ")
    
    if choice == 'a':
        patient.first_name = input("Enter new first name: ")
        patient.last_name = input("Enter new last name: ")
    elif choice == 'b':
        patient.address = input("Enter new address: ")
    elif choice == 'c':
        patient.phone_number = input("Enter new phone number: ")
    elif choice == 'd':
        patient.emergency_contact_name = input("Enter new emergency contact name: ")
    elif choice == 'e':
        patient.emergency_contact_num = input("Enter new emergency contact number: ")
    else:
        print("Invalid choice [a-e]")


def add_procedure(patient):
    """adds procedure to patient"""
    name = input("Enter procedure name: ")
    doctor = input("Enter doctor's name: ")
    date = input("Enter procedure date: ")
    cost = float(input("Enter procedure cost: "))
    
    procedure = medical.Procedure(name, doctor, date, cost)
    patient.add_procedure(procedure)
    print(f"Procedure {procedure._id} added to patient {patient._id}")


def patient_lookup():
    """patient lookup, allows for patient alterations if id lookup successful"""
    pid = input("Enter patient ID number: ")
    patient = medical.Patient.get_patient(pid)

    try:
        pid = int(pid)
        patient = medical.Patient.get_patient(pid)
    except ValueError:
        print("Invalid ID format")
        return
    
    if patient:
        print(patient)
        while True:
            patient_option = input("a. Modify a patient's attributes\n"
                                   "b. Delete a patient\n"
                                   "c. Add a procedure\n"
                                   "d. Return to main menu\n"
                                   "Enter choice: ")
            if patient_option == 'a':
                modify_patient(patient)
            elif patient_option == 'b':
                medical.Patient.delete_patient(pid)
                print("Patient deleted.")
                return
            elif patient_option == 'c':
                add_procedure(patient)
            elif patient_option == 'd':
                break
            else:
                print("Invalid input [a-d]")
    else:
        print("Patient not found.")

def main():
    """main driver func"""
    while True:
        user_in = get_choice()
        if user_in == '1':
            patient_lookup()
        elif user_in == '2':
            create_patient()
        elif user_in == '3':
            print("Data saved. Exiting...")
            medical.Patient.save_patients()
            break
        else:
            print("Invalid input, please enter a choice [1-3]")


if __name__ == "__main__":
    main()
