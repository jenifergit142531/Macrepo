def decor1(func):
    def inner():
        x=func()
        return x*x
    return inner

def decor2(func):
    def inner():
        x=func()
        return 2*x
    return inner

@decor1
@decor2
def num():
    return 10


print(num())

# logic : decor1(decor2(no))










"""def hello_decorator(func):
    def inner1(*args,**kwargs):
        print("before execution")
        call_function = func(*args,**kwargs)
        print("after execution")
        return call_function
    return inner1

@hello_decorator
def sum_two_numbers(a,b):
    print("Inside the function")
    return a+b
print("sum = ",sum_two_numbers(10,20))"""