 #Class Attribute 

class Student:
    collage ="ABC Collage"

    def __init__(self , name , rollNumber, age, state):
        self.name = name
        self.rollNumber = rollNumber
        self.age = age
        self.state = state

    def information(self):
        print(f"Student Name is {self.name}")
        print(f"Student RollNumber is {self.rollNumber}")
        print(f"Student Age is {self.age}")
        print(f"Student State is {self.state}")
        print(f"Student Collage is {Student.collage}")

    def assignment(self):
        print(f"{Student.collage} is finally completed there assignment")
        print(f"{self.name} has completed there assignment whose rollNumber is {self.rollNumber}");

stu = Student("Gaurav", 1, 22,"Madhya Pradesh");
stu.information();
stu.assignment();


# Instance Attribute

class Student:
    def __init__(self , name , rollNumber, age, state):
        self.name = name
        self.rollNumber = rollNumber
        self.age = age
        self.state = state

    def information(self):
        print(f"Student Name is {self.name}")
        print(f"Student RollNumber is {self.rollNumber}")
        print(f"Student Age is {self.age}")
        print(f"Student State is {self.state}")

    def assignment(self):
        print(f"{self.name} has completed there assignment whose rollNumber is {self.rollNumber}");

stu = Student("John doe", 3, 22,"Andhra Pradesh");
stu.information();
stu.assignment();




# Static Method
class MathOperations:

    @staticmethod
    def add_numbers(a, b):
        return a + b


# Using the static method without creating an instance
# Accessing static method using class name
result = MathOperations.add_numbers(5, 3)
print(result)

# Accessing static method using an object reference
math_op = MathOperations()
print(math_op.add_numbers(10, 5))



# Class Method
class Student:
    college_name = "ABC University"

    def __init__(self, name, age, roll_number):
        self.name = name
        self.age = age
        self.roll_number = roll_number

    @classmethod
    def change_college_name(cls, new_name):
        cls.college_name = (
            new_name  # Modifying class attribute using class method
        )

    def attend_class(self):
        print(f"{self.name} from {Student.college_name} is attending the class.")


# Changing the class attribute using a class method
Student.change_college_name("XYZ University")

# Creating Student objects
student_1 = Student("Amit", 20, "S123")
student_2 = Student("Priya", 19, "S124")

student_1.attend_class()
student_2.attend_class()

# Accessing class method using an object reference
student_1.change_college_name("New University Name")

# Accessing class attribute directly through class name
print(Student.college_name)