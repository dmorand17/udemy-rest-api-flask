def methodception(another):
    return another()

def add_to_numbers():
    return 35+77

#print(methodception(add_to_numbers))
#print(methodception(lambda: 35+77))

my_list = [13,56,77,108,484]

print(list(filter(lambda x: x != 13, my_list)))