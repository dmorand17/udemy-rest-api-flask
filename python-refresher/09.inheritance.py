class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / sum(len.marks)

    @classmethod
    def friend(cls, origin, friend_name, *args, **kwargs):
        return cls(friend_name,origin.school, *args, **kwargs)

##

class WorkingStudent(Student):
    def __init__(self, name, school, salary, job_title):
        super().__init__(name, school)
        self.salary = salary
        self.job_title = job_title


anna = WorkingStudent("Anna", "Oxford", "50,000", "Software Developer")
friend = WorkingStudent.friend(anna,"Greg",10000, job_title="Software Architect")

print(anna.salary)
print(friend.name)
print(friend.school)
print("friend salary {}".format(friend.salary))