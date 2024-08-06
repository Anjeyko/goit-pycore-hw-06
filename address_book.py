from collections import UserDict

class AddressBook(UserDict):
    
    def add_record(self, record):
        self.data[record.name.value] = record
        print(f"Contact added")

    def find(self, name):
        try:
            record = self.data[name]
            return record
        except KeyError:
            return f"There is no contanct with name {name}"

    def delete(self, name):
        try:
            del self.data[name]
            print(f"Contact {name} deleted")
        except KeyError:
            return f"There is no contanct with name {name}"