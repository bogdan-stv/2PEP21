from collections import UserString, Counter

class InformationGetter(UserString):

    def information(self):
        my_data = Counter(self.split())
        for key in my_data.keys():
            if len(key) <= 3:
                my_data[key] = 0
        print(my_data)
        sum = 0
        for value in my_data.values():
            sum = sum + value
        average = sum / len(my_data.keys())
        max_deviation = average * (200 / 100)
        for key in my_data.keys():
            if my_data[key] > max_deviation:
                print(key)


with open("data.txt") as f:
    file_data = f.read()
getter = InformationGetter(file_data)
getter.information()


