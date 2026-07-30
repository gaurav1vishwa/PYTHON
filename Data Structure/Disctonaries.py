# disctonaries mutable , {key : value} , key - uniue (duplicated replaceable);

# creating the disctonary 

student = {
    "name" : "Gaurav",
    "age" : 23,
    "city" : "Bangalore",
    "State": "karnatka"
}
print(student);

# inserting the value in the disctonary
student["phoneNumber"] = "3309876549";
print(student);
student["isMarried"] = False;
print(student);

# to remove the specific elemnt/item from the disctonary with the help fo the key 
student.pop("city");
print(student);

# to check the datatype 
print(student, type(student));

# to print the value based on the key , i mean to get the item/element
print(student["age"]);
print(student.get("age"));
# it will gave the error because there is no key wht the city because we already pop it out i mean the key ,    print(student["city"]); 

# it will pop out the item from the disctonary at last , and return the poped element;
print(student.popitem());
print(student);

# delete the item ,  but not return anything like the deleted item
del student["age"];
print(student);

# delete the whole disctonary
student.clear();
print(student);

student = {
    "name" : "Gaurav",
    "age" : 23,
    "city" : "Bangalore",
    "State": "karnatka"
}

# update the item form the disctonary
student.update({"age":22, "city":"Bhopal"});
print(student);

#print the key or value or item
print(student.keys()); # gives all the keys
print(student.values()); # gives all the values
print(student.items()); # gives list of all the items

# print key and values using the for loop
for key, value in student.items():
    print(key, ":", value);

# copy the disctonary to the new one
new_stu = student.copy();
print(new_stu);

# new_stu = student.clear();# it will give the NONE 
# print(new_stu);


#Nexted Disctonary
student = {
   "student1" : {
       "name" : "gaurav",
       "age" : 22,
       "state" : "M.P"

   },
   "student2" : {
        "name" : "Rahul",
              "age" : 23,
              "state" : "Andra.P"
   },
   "student3" : {
        "name" : "Shyam",
              "age" : 32,
              "state" : "U.P"
   }
}

print(student);

print(student["student1"]["name"]);
print(student["student3"]["state"]);

for key, value in student.items():
    print(key, ":", value);


for student_id, details in student.items():
    print(student_id)
    for key, value in details.items():
        print(" ", key, ":", value)
    print()  # blank line between students

