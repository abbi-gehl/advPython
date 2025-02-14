# Abigail Gehlbach
# lab 04 supporting file

import pickle


class Patient:
    _next_id = 100
    _all_patients = {}

    @classmethod
    def get_patient(cls, pid):
        try:
            return cls._all_patients[pid]
        except KeyError:
            return None
        except TypeError:
            return None
        else:
            return None

    @classmethod
    def delete_patient(cls, pid):
        try:
            del cls._all_patients[pid]
            return
        except KeyError:
            return None
        else:
            return None

    @classmethod
    def save_patients(cls):
        pickle.dump(cls._all_patients, open("save.p", "wb"))

    def __init__(self, first_name, last_name, address, phone_number, emergency_contact_name, emergency_contact_num):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone_number = phone_number
        self.emergency_contact_name = emergency_contact_name
        self.emergency_contact_num = emergency_contact_num
        self.procedures = []
        self._id = Patient._next_id
        Patient._next_id += 1
        Patient._all_patients[self._id] = self

    def __str__(self):
        procs = ""
        for procedure in self.procedures:
            procs += str(procedure) + "\n"
        return(f"Patient Name: {self.first_name} {self.last_name}, ID: {self._id}\n"
               f"Address: {self.address}, Phone: {self.phone_number} \n"
               f"Emergency Contact: {self.emergency_contact_name}, {self.emergency_contact_num}\n"
               f"Patient Procedures:\n{procs}")

    def add_procedure(self, proc):
        self.procedures.append(proc)


class Procedure:
    _next_id = 1000

    def __init__(self, name, doctor, date, cost):
        self.name = name
        self.doctor = doctor
        self.date = date
        self.cost = cost
        self._id = Procedure._next_id
        Procedure._next_id += 1

    def __str__(self):
        return(f"Procedure {self._id}: {self.name} | Doctor: {self.doctor}\n"
               f"Date: {self.date} | Cost: {self.cost}")


p1 = Patient("Abigail", "Gehlbach", "123 abc street", "111-222-3345", "my dad", "123-333-2314")
print(p1)

p2 = Patient("Clare", "McCaffrey", "456 xyz rd", "333-371-2373", "her dad", "152-628-4871")
print(p2)

proc1 = Procedure("lung extensions", "Dr. Crowbar", "4/20/2025", 100000.87)
proc2 = Procedure("new tummy", "Dr. tummy", "3/21/2025", 20000.55)

p1.add_procedure(proc1)
p2.add_procedure(proc2)

print(Patient.get_patient(100))
print(Patient.get_patient(101))
