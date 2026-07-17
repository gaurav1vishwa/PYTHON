print("---------------Arithmetic Operators-----------------");
a = 20;
b = 10;
print("Addition:", a + b); # 30
print("Subtraction:", a - b); # 10
print("Multiplication:", a * b); # 200
print("Division:", a / b); # 2.0
print("Floor Division:", a // b); # 2
print("Modulus:", a % b); # 0
print("Exponentiation:", a ** b); # 10240000000000  , a to power of b that is the meening of exponentiation operator


print("---------------Comparison Operators-----------------");

x = 10;
y = 20;
print("x is equal to y:", x == y); # False
print("x is not equal to y:", x != y); # True
print("x is greater than y:", x > y); # False
print("x is less than y:", x < y); # True
print("x is greater than or equal to y:", x >= y); # False
print("x is less than or equal to y:", x <= y); # True


print("---------------Logical Operators-----------------");

p = True;
q = False;
print("p and q:", p and q); # False
print("p or q:", p or q); # True    
print("not p:", not p); # False
print("not q:", not q); # True

print("---------------Assignment Operators-----------------");

num = 10;
print("Initial value of num:", num); # 10
num += 5; # num = num + 5
print("After += 5, num:", num); # 15
num -= 3; # num = num - 3
print("After -= 3, num:", num); # 12
num *= 2; # num = num * 2
print("After *= 2, num:", num); # 24
num /= 4; # num = num / 4
print("After /= 4, num:", num); # 6.0
num //= 2; # num = num // 2
print("After //= 2, num:", num); # 3

print("---------------Identity Operators-----------------");

a = 10;
b = 10;
c = 15;
print("a is identical to b:", a is b); # True
print("b is identical to c:", b is c); # False
print("a is not identical to c:", a is not c); # True

print("---------------Membership Operators-----------------");

number = [1, 2, 3, 4, 5];
print("3 is in number:", 3 in number); # True
print("6 is not in number:", 6 not in number); # True
print("4 is in number:", 4 in number); # True
print("2 is not in number:", 2 not in number); # False
print("1.5 is in number:", 1.5 in number); # False

print("---------------Bitwise Operators-----------------");

x = 10; # 1010 in binary
y = 4;  # 0100 in binary
print("x & y:", x & y); # 0 if both digit are 1 then it will return 1 otherwise it will return 0
print("x | y:", x | y); # 14 if one of the digit is 1 then it will return 1
print("x ^ y:", x ^ y); # 14  if both dight are same then it will return 0 and if both digit are different then it will return 1
print("~x:", ~x); # -11   
print("x << 1:", x << 1); # 20
print("x >> 1:", x >> 1); # 5


