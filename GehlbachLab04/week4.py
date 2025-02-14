import medical


def get_choice():
    # get input, no cleaning
    return input("1. Look up a patient by ID number.\n"
                 "2. Add a new patient\n"
                 "3. Quit\n"
                 "Please enter your choice: ")


def create_patient():
    person_list =


def modify_patient():
    input("1. Change patient name\n"
          "2. Change patient address\n"
          "3. Change patient phone\n"
          "4. Change emergency contact name\n"
          "Input choice: ")




def patient_lookup():
    pid = input("Enter patient ID number: ")
    patient = medical.Patient.get_patient(pid)

    if patient:
        while True:
            patient_option = input("(a) modify a patient's attributes, "
                                   "(b) delete a patient, or "
                                   "(c) add a procedure"
                                   "Enter choice: ")
            if patient_option == 'a':
                # code
            elif patient_option == 'b':
                medical.Patient.delete_patient(pid)
                return
            elif patient_option == 'c':
                # test
            else:
                print("Invalid input")


def main():
    while True:
        user_in = get_choice()
        if user_in == '1':
            patient_lookup()
            print('a')
        elif user_in == '2':
            # do thing
            print('b')
        elif user_in == '3':
            medical.Patient.save_patients()
            break
        else:
            print("Invalid input, please enter a choice [1-3]")


if __name__ == "__main__":
    main()
