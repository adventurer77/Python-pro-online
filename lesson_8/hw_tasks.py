#  Task 1 

def generate_sequence(n, first_value, gen_func):
  """
   Generator function for a number sequence.

   Args:
     n: Number of sequence members.
     first_value: Initial value.
     gen_func: Function that generates the next member of the sequence.

   Yields:
     Consecutive members of a number sequence.
   """
  current_value = first_value
  yield current_value

  for _ in range(1, n):
    current_value = gen_func(current_value)
    yield current_value

# Пример использования
def next_fib(n):
  return n + n - 1

sequence = generate_sequence(10, 0, next_fib)

for value in sequence:
  print(value)



# Task 2

import time

def fibonacci_recursive(n):
  """A simple recursive Fibonacci function."""
  if n == 1 or n == 2:
    return 1
  return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

start_time = time.time()
n = 35
result_recursive = fibonacci_recursive(n)
print(f"Recursive: Fibonacci Number {n} = {result_recursive}, lead time: {time.time() - start_time:.2f} second")


def fibonacci_memoization(n):
  """Recursive Fibonacci function with memoization."""

  if n in cache:
    return cache[n]

  result = fibonacci_memoization(n - 1) + fibonacci_memoization(n - 2)
  cache[n] = result
  return result

cache = {1: 1, 2: 1}
n = 35
start_time = time.time()
result_memoization = fibonacci_memoization(n)
print(f"Memoized: Fibonacci Number {n} = {result_memoization}, lead time: {time.time() - start_time:.2f} second")

# def fibonacci_memoization_optimized(n):
#   """
#   Оптимизированная рекурсивная функция Фибоначчи с мемоизацией.
#   """
#   if n == 1 or n == 2:
#     return 1

#   if n in cache:
#     return cache[n]

#   if n % 2 == 0:
#     result = fibonacci_memoization_optimized(n // 2) * fibonacci_memoization_optimized(n // 2)
#   else:
#     result = (fibonacci_memoization_optimized((n - 1) // 2) + fibonacci_memoization_optimized((n + 1) // 2)) * 2

#   cache[n] = result
#   return result

# cache = {}
# n = 35
# start_time = time.time()
# result_memoization_optimized = fibonacci_memoization_optimized(n)
# print(f"Оптимизированная мемоизация: Число Фибоначчи {n} = {result_memoization_optimized}, время выполнения: {time.time() - start_time:.2f} секунд")


# Task 3

import random

def pow_2(item):
    return item ** 2

def my_sequence(sequence,func):
    return sum(func(item) for item in sequence)

x = [random.randint(1, 10) for _ in range(10)]
print(x)
print(my_sequence(x, pow_2))