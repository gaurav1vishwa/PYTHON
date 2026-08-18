class Student:
    def __init__(self):
        self.name = "Gaurav"   # public

student = Student()

print(student.name)           # ✅ Allowed
student.name = "Rahul"        # ✅ Allowed
print(student.name)




class University:
    name = "APSU";

u = University();
print(u.name);