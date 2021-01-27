# Define a function
def func1():
    print("I am a function")
# func1()
# print(func1)

# Function that takes arguments
def func2(arg1, arg2):
    print(arg1, " ", arg2)
# func2(10, 20)

# Function that returns a value
def cube(x):
    return x*x
# print(cube(5))

# Function with default value for an argument
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result
# print(power(2))
# print(power(2, 2))
# print(power(x = 3, num = 2))

# Function with variable number of arguments
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result
print(multi_add(4, 5, 10, 4))
