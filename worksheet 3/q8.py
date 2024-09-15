#Define a Python function student(). Using function attributes display the names of all arguments. 

def student(name, age, grade):
    pass

# Access function arguments using the `__code__.co_varnames` attribute
print("Function argument names:", student.__code__.co_varnames)