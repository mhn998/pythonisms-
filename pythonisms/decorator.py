# use of decorator in debugging functions input and output / calculate a time for running a function and how many times to run it
import time

def factorial(n):
  if n == 0:
    return 0

  else:
    return n * factorial(n-1)

starting_time = time.time()
factorial(50)
ending_time = time.time()

# print(ending_time-starting_time)
def calculate_time(any_fun):
  
  def wrapper(*args,**kwargs):
    starting_time = time.time()
    result = any_fun(*args,**kwargs)
    ending_time = time.time()
    print (ending_time-starting_time)
    return result
  return wrapper


def debug_code(any_fun):
  def wrapper(*arg, **kwargs):
    x = arg
    y = kwargs
    print(f'inputs are : {x}, {y}')
    output = any_fun(*arg, **kwargs)
    print(f'output is : {output}')
    return output

  return wrapper

@debug_code
def fibbnacci(n):
  if n == 0:
    return 0
  if n == 1:
    return 1
  return fibbnacci(n-1)+ fibbnacci(n-2)

fibbnacci(3)





@calculate_time
def fibbnacci(n):
  if n == 0:
    return 0
  if n == 1:
    return 1
  return fibbnacci(n-1)+ fibbnacci(n-2)

fibbnacci(3)

def run_n(*args, **kwargs):
  n = args[0]
  
  def inside(fun):
    
    def extra():
      pass

    for i in range(n-1):
      fun()
    return fun

  return inside


@run_n(3)
def print_hello():
  print("hello world")

print_hello()