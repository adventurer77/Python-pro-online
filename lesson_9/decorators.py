# Task 1

def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.num_calls += 1
        return func(*args, **kwargs)
    wrapper.num_calls = 0
    return wrapper

@count_calls
def my_func():
    print("Who are you ???")

my_func()
my_func()
my_func()

print(my_func.num_calls)


# Task 2

my_function = []

def add_function(f):
    my_function.append(f)
    return f

 
@add_function
def my_list(x):
 return x 


@add_function
def my_second_list(y):
   return y

x  = [i for i in range (1,5)]
y = [i for i in range (1,5)]

print(my_function)



# Task 3


def save_res_to_file(func):

    def wrapper(self):
        filename = f"{type(self).__name__}.txt"

        with open(filename, "a") as file:
            file.write(f"{func(self)}\n")
                # return "File save"
        return func(self)
                
    return wrapper
    
 

class BankStr:
    def __init__(self,my_str):
        self.my_str = my_str

    @save_res_to_file
    def __str__(self) -> str:
        return self.my_str
    
print(BankStr("hello"))

# Task 4

import time

def timer(quantity,my_file):
    def decorator(func):
        def wrapper(*args, **kwargs):
            s_time = 0
            with open(my_file,"w") as file:
                for i in range(quantity):
                    start_time = time.monotonic()
                    result = func(*args, **kwargs)
                    end_time = time.monotonic()
                    run_time = end_time - start_time
                    s_time += run_time
                    file.write(f"Start {i+1} : {run_time:.4f} - second\n")
                s_time /= quantity
                file.write(f"Quantity = {quantity} : {run_time:.4f} - second\n")
                return result
        return wrapper
    return decorator


@timer(quantity=10, my_file="results.txt")
def my_function():
    return "Time"

my_function()




