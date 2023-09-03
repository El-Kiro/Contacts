class Field:
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def delete_phone(self, phone):
        self.phones = [p for p in self.phones if str(p) != phone]

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if str(p) == old_phone:
                p.value = new_phone

    def __str__(self):
        phones_str = ", ".join(str(p) for p in self.phones)
        return f"Name: {self.name}, Phones: {phones_str}"


class AddressBook(dict):
    def add_record(self, record):
        self[record.name.value] = record

    def search_records(self, **kwargs):
        results = []
        for name, record in self.items():
            match = True
            for key, value in kwargs.items():
                if key == 'phone':
                    if all(str(phone) != value for phone in record.phones):
                        match = False
                        break
                else:
                    if str(getattr(record, key).value) != value:
                        match = False
                        break
            if match:
                results.append(record)
        return results

