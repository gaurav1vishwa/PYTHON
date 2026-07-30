# Tuples , immutable, collection of items , order and unordered, 

days_of_week = ("Monday", "Tuesday", "Wednesday","Thursday","Friday","Saturday");
print(days_of_week);

# access the particular value from the tuple using the indexing number

print(days_of_week[0]);
print(days_of_week[3]);


# use tuple for the immutablity
# efficiency
# return multiple values


# returning multiple values
def get_student_info():
    name = 'gaurav';
    age = 23;
    location = "Madhya pradesh";
    return (name, age, location);

student_info = get_student_info();
print(student_info);

# packing and unpacking int the touple

#packing means to putting multiple values into a single tuple, like 
student = ("gaurav", 22,'phython');
print(student)

# unpacking allows us to take those values out of the tuple and assign them to separte variable (immutable but flaxiable)

name , age , course = student;
print(name);
print(age);
print(course);


# concatenating touple to make new touple

tuple1 = (1,2,3);
tuple2 = (4,5,5);
combined = tuple1 + tuple2;
print(combined);

# you can use the *  operator to repeat the tuple for multiple time
tuple4 =("hello",)*5;
print(tuple4) # 5 times hello will be created ;
