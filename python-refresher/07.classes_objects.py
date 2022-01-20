lottery_player_dict = {"name": "Rolf", "numbers": (5, 19, 12, 56)}


class LotteryPlayer:
    def __init__(self, name, numbers):
        self.name = name
        self.numbers = numbers

    def total(self):
        return sum(self.numbers)


player_one = LotteryPlayer("Rolf", (5, 10, 6, 7, 11))
player_two = LotteryPlayer("John", (7, 12, 8, 11, 19))

print(player_one == player_two)


class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    @classmethod
    def go_to_school(cls):
        print("Going to school as {}".format(cls))

    @staticmethod
    def static_go_to_school():
        print("I'm going to school")


anna = Student("Anna", "MIT")
rolf = Student("Rolf", "Oxford")
anna.marks.append(56)
anna.marks.append(78)

Student.go_to_school()
anna.static_go_to_school()

print(anna.marks)
print(anna.average())
