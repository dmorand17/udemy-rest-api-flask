import functools

def my_decorator(func):
    @functools.wraps(func)
    def function_that_runs():
        print("Having fun...")
        func()
        print("After the fun...")
    return function_that_runs

@my_decorator
def my_function():
    print("My function...")

my_function()

def decorator_with_args(num):
    def my_decorator(func):
        @functools.wraps(func)
        def function_that_runs():
            print("In decorator")
            if num == 56:
                print("Not running...")
            else:
                func()
            print("after decorator")
        return function_that_runs
    return my_decorator


@decorator_with_args(56)
def my_function_two():
    print("Hello")

my_function_two()