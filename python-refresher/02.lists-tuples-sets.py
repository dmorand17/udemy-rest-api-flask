my_variable = "hello"
grades = [77, 80, 90, 95, 100]
tuple_grades = (77, 80, 90, 95, 100) # immutable
set_grades = {77, 80, 100, 90, 100} # set

print(sum(grades) / len(grades))

print(set_grades)
grades.append(100)
print(grades)

tuple_grades = tuple_grades + (100,)
print(tuple_grades)

grades[0] = 65
print(grades)

your_lottery_numbers = {1,2,3,4,5}
winning_numbers = {1,3,5,7,9,11}

print(your_lottery_numbers.intersection(winning_numbers))
print(your_lottery_numbers.union(winning_numbers))
print({1,2,3,4}.difference({1,2}))

###### Coding Exercise ########

my_list