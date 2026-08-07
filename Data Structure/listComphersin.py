# function to find square of a number 

number  =[1,2,3,4,5,6,7,8,9];
double = [];
for num  in number:
    double.append(num * num);

print(double);


# List Comprehension  - listname = [expression for item in iterable if condition == True]
double = [num * num for num in number];
print(double);

number = [1,2,3,4,5,6,7,8,9];
result = [x if x % 2 == 0 else "odd" for x in number];
print(result);

even = [n for n in number if n % 2 == 0];
print(even);
