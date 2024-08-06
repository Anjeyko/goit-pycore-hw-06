from name import Name
from phone import Phone

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        self.phones.append(Phone(phone_number))
    
    def edit_phone(self, old_number, new_number):
       self.phones = [Phone(new_number) if phone.value == old_number else phone for phone in self.phones]

    def remove_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                self.phones.remove(phone)

    def find_phone(self, number):
        for phone in self.phones:
            if phone.value == number:
                return phone
 

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"