"""
Medical.py file for patient and procedure classes delcaration
uses pickle to save information to save.p file and load when opened again

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
import pickle


class Patient:
    _next_id = 100
    _all_patients = {}

    @classmethod
    def get_patient(cls, pid):
        return cls._all_patients.get(pid, None)

    @classmethod
    def delete_patient(cls, pid):
        if pid in cls._all_patients:
            del cls._all_patients[pid]
    
    @classmethod
    def save_patients(cls):
        pickle.dump(cls._all_patients, open("save.p", "wb"))

    @classmethod
    def load_patients(cls):
        try:
            with open("save.p", "rb") as f:
                cls._all_patients = pickle.load(f)
            if cls._all_patients:
                cls._next_id = max(cls._all_patients.keys()) + 1
        except (FileNotFoundError, EOFError):
            cls._all_patients = {}
            cls._next_id = 100

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

    @classmethod
    def update_next_id(cls, patients):
        max_proc_id = max((proc._id for p in patients.values() for proc in p.procedures), default=999)
        cls._next_id = max_proc_id + 1

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

def initialize_data():
    Patient.load_patients()
    Procedure.update_next_id(Patient._all_patients)