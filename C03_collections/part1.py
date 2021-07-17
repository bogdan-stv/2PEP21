from collections import UserString, Counter

class My_str(UserString):

    def my_method(self, text):
        if text in self:
            print("text is there")

my_str = My_str("initial String")
print(my_str)
my_str.my_method('Str')

#----------------------------#

my_text = "the fox is in the tree"
counter = Counter()

for word in my_text.split():
    counter[word] += 1

my_new_text = "there is no fox in the tree"
for word in my_new_text.split():
    counter[word] -= 1

print(counter)

#-------------------------------#
# information

x = 1,2,3
y = 1,2,3,  1,2,3

#----------------------------------#

from collections import deque

my_dq = deque([1,2,3], 3)
my_dq.append(4) # inlocuieste ultimul element cu 4
my_dq.appendleft(5)
print(my_dq)

#-----------------------------------#

from collections import OrderedDict

dict_1 = {1:"1", 2:"2", 3:"3"}
dict_1[0] = "0"
print(dict_1)
dict_2 = OrderedDict({"1":1, "2":2})
print(dict_2)



