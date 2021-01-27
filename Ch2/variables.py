# Declare a variable
f = 0
# print(f)

# Re-declaring the variable
f="abc"
# print(f)

# ERROR: variables of different types cannot be combined
# print("This is a string " + str(123))

# Global vs. local varibles in functions
def someFunction():
    global f
    f="def"
    print(f)

someFunction()
print(f)

del f
