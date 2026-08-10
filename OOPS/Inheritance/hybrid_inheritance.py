# combinataion of two or more types of inheritance is called hybrid inheritance

class A:
    def method(self):
        return "Method A from class A"

class B(A):
    def method(self):
        return "Method B from class B"

class C(A):
    def method(self):
        return "Method C from class C"

class D(B, C):
    pass

d = D();
print(d.method()) # it is resolved by the help of MRO (Method Resolution Order) and it will call the method of class B because class B is inherited first in class D.