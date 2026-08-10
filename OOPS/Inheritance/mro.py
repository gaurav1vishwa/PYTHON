class A:
    def show(self):
        print("This is a");

class B(A):
    def show(self):
        print("This is b");

class C(A):
    def show(self):
        print("This is c");


class D(B, C):
    pass

d = D();
d.show();

print(D.mro());


#MRO Question
class A:
    def show(self):
        print("This is a");

class B(A):
    def show(self):
        print("This is b");

class C(A):
    def show(self):
        print("This is c");

class D(B, A):
    def show(self):
        print("This is d");

class E(C, A):
    def show(self):
        print("This is e");

class F(D, E):
    def show(self):
        print("This is f");

obj = F();
obj.show(); # This is f
print(F.mro()); # F,D,B,E,C,A,object