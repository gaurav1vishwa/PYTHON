#Operator overloading --Dunder method , maginc method
# + __add__()
# - __sub__()
# * __mul__()

class Student:
    def __init__(self, marks):
        self.marks = marks;

s1 = Student(50);
s2 = Student(30);
print(s1); # print the address 
print(s2); # print the address
#print(s1 + s2); # error because address can't to be added;

# to over come this problem we use the Dunder(magic) method

class Student1:
    def __init__(self, marks):
        self.marks = marks;

    def __add__(self, other):
       return Student1(self.marks + other.marks);

s1 = Student1(50);
s2 = Student1(30);
s3 = Student1(40);
# print(s1.marks);
# print(s2.marks);
# print(s1.marks + s2.marks);

res = s1 +s2 +s3;
print(res.marks);


class Person:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def __gt__(self, other):
        return self.mark > other.mark


p1 = Person("Gaurav", 21)
p2 = Person("Shni", 64)

if p1 > p2:
    print(f"{p1.name} is greater than the other")
else:
    print(f"{p2.name} is greater than the other")