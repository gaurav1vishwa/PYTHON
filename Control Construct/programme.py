
# conditional statement (if else ) and else if ladder

name = "gaurav";
if name == "gaurav":
    print("Hello gaurav")
elif name == "shni":
    print("Hello shni")
else:
    print("Hello stranger")


name = "alice";
age = 20;

if name =="alice":
    if age >= 18:
        print("Hello alice, you are an adult.")
    else:
        print("Hello alice, you are a minor.")
else:
    print("Hello stranger.")  



    # loop (for, while)

for  i in range(1,6):
    print(i);      

# while loop
saving = 0
while saving < 500:
    saving += 100
    print("Saving:", saving);


 # break, continue, return
for i in range(1, 11):
    if i == 5:
        break  # Exit the loop when i is 5
    print(i);  


i = 1;
while i < 10:
    i += 1;
    print(i);
    if i ==5:
        continue;


# pass statement  we can use it as the placeholder and latter we can use 
for i in range(1, 6):
    if i == 4:
        pass# we can use it latter;
    else:
        print(i);    

# return 

def function(name):
    if not name:
        return "you are strangers";
    return f"hello {name}";


print(function("gaurav"));
print(function(""));