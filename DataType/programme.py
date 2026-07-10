# primitive Common

a = 10;
print(a);

a= -5;
print(a);

print(a, type(a));


# 1. Numeric Data Types
a = 10          # int
b = 10.5        # float
c = 3 + 4j      # complex
print(a, type(a))
print(b, type(b))
print(c, type(c))



# 3. Boolean (bool)
is_pass = True
is_fail = False

print(is_pass, type(is_pass))
print(is_fail, type(is_fail))



# 2. String (str)
name = "Gaurav"
city = 'Bhopal'

print(name)
print(city)


info = """This is a multi-line string.
It can span multiple lines."""
print(info)

print();

info2 = '''This is another multi-line string.
It can also span multiple lines.''' 
print(info2)


# single "" is not working for the multi-line string, but single '' is working for the multi-line string.
info3 = """This is
 a string with a single
 quote: ' and a 
double quote: \""""
print(info3)


