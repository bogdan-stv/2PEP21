from collections import OrderedDict


class Phonebook:

    def __init__(self):
        self.phonebook = OrderedDict()

    def add_number(self, name, number):
        self.phonebook[name] = number
        for key in self.phonebook.copy().keys():
            if key > name:
                self.phonebook.move_to_end(key)

    def remove_number(self):
        self.phonebook.popitem()


phonebook = Phonebook()
phonebook.add_number("Maria", "0720543505")
phonebook.add_number("Ion", "0725543505")
phonebook.add_number("Aon", "0725543505")
phonebook.add_number("Bon", "0725543505")
phonebook.add_number("Zon", "0725543505")
phonebook.add_number("Fon", "0725543505")
# phonebook.remove_number()

print(phonebook.phonebook.items())
