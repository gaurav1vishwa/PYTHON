#method with same name but different parameters is called method overloading (compile time polymorphism)
# but python does not support method overloading by default, 
# we can achieve it by using default arguments or variable-length arguments.


# class Calculator:
#     def add(a,b):
#         return a + b
#     def add(a,b,c):
#         return a + b + c
#     def add(a,b,c,d):
#         return a + b + c + d

# c = Calculator()
# print(c.add(1,2))  # This will raise an error because the last defined method will override the previous ones



# This will work because we are using variable-length arguments *agrgs means 
# we can pass any number of argumnets to the method and it will return the sum of all the arguments passed to it.

class Test:
    def add(self, *args):
        return sum(args)


t = Test()
print(t.add(1, 2))        # Output: 3
print(t.add(1, 2, 3))     # Output: 6
print(t.add(1, 2, 3, 4))  # Output: 10