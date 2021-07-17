"""
Counted List
Create a class for an list like object based on UserList wrapper
That object should have a method to return a Counter for all objects in the list
Counter should be updated automatically for at lest 2 methods (append, pop)
"""

from collections import UserList, Counter

class MyList(UserList):

    def __init__(self, list):
        super().__init__(list)
        self.counter = Counter()

    def get_counter(self):
        self.counter = Counter(self)
        return self.counter

    def append(self, value):
        super().append(value)
        self.counter[value] += 1

    def remove(self, value):
        if self.counter[value] == 1:
            del self.counter[value]
        else:
            self.counter[value] -= 1
        super().remove(value)

    def pop(self, i):
        if self.counter[self[i]] == 1:
            del self.counter[self[i]]
        else:
            self.counter[self[i]] -= 1
        super().pop(i)


my_list = MyList([1, 2, 3, 4])
counter = my_list.get_counter()
my_list.append(5)
my_list.remove(4)
my_list.pop(0)
print(my_list, counter)