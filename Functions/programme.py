def print_greeting(name, age, city, country):
    print(f"Hello, {name}! You are {age} years old and live in {city}, {country}.")

print_greeting("Alice", 30, "New York", "USA")


# DIFFERENT TYPE OF FUNCTION
#1. NO ARGUMENTS AND NO RETURN VALUE

def function_no_args_no_return():
    print("This function takes no arguments and returns nothing.");


#2. NO ARGUMENTS BUT RETURNS A VALUE

def function_no_args_returns_value():
    return "This function takes no arguments and returns a value.";


#3. TAKES ARGUMENTS BUT RETURNS NOTHING
def function_args_no_return(arg1, arg2):
    print(f"This function takes arguments: {arg1} and {arg2}, but returns nothing.");

#4. TAKES ARGUMENTS AND RETURNS A VALUE
def function_args_returns_value(arg1, arg2):    
    return f"This function takes arguments: {arg1} and {arg2}, and returns a value.";


# calling  the functions
function_no_args_no_return()
print(function_no_args_returns_value())
function_args_no_return("Hello", "World")
print(function_args_returns_value("Python", "Programming"))
