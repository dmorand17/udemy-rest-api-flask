def my_method(*args,**kwargs):
    return sum(args)

def what_are_kwargs(*args,**kwargs):
    print(args)
    print(kwargs)

print(my_method(5,11,90,100))

what_are_kwargs(50,20,10,name='Jose', location='UK')