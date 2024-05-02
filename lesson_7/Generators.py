# Task 1

def gen_geom_progression(start, q, n):
    for _ in range(n):
        yield start
        start *= q

res = gen_geom_progression(2, 2, 10)
for item in res:
    if item == 64:
       res.close() 
    print(item)

print(list(gen_geom_progression(2, 2, 10)))



#  Task 2

def my_range(my_number,border=0,step=0):
    """Generator function similar to the range function.
    
    Args:
        my_number (int): Start number of the range.
        border (int): Ending number of the range.
        step (int): Step number of the range.

    Yields:
        int: Returns numbers in a sequence within a given range. 
    """

    if step > 0:
        while  my_number <= border - 1:
            yield  my_number  
            my_number += step
    elif step < 0:
        while  border <= my_number - 1  :
            yield  my_number 
            my_number += step
    elif step == 0 and border != 0:
        while  my_number <= border - 1:
            yield  my_number 
            my_number += 1
    else:
        while  border <= my_number - 1  :
            yield  border
            border += 1


res = my_range(2,-14,-2)
print(list(res))


# Task 3
def gen_prime_numbers(n):
    for n in range(2, n + 1):
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            yield n


print(*gen_prime_numbers(100))

# Task 4
n = int(input("Enter the number >> "))
mylist = [x**3 for x in range(2,n+1)]

print(mylist)

print(list(pow(x,3) for x in range(2,(int(input("Enter border>> "))+ 1))))

