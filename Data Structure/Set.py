# SET =>  unordered, home/hetro genious both , dosen't allow duplicates, no index 

# declearing set and printing
set1 = {"apple","banana","guava","apple"};
print(set1);


#give error becuase set object does not supports the assignment
#set1[3] ="orange";
#print(set1);

#adding items in sets 

set1.add("orange");
print(set1);

#removing items insets  , if element not found it gave error
set1.remove("apple");
print(set1);

# descard elemtn from the set 
# if element not found it print no error
set1.discard("apple");
 # set1.remove("apple"); keyerror "apple";
print(set1);

print(set1, type(set1));

#pop is used to remove the rendome items from the set 
set1.pop();
print(set1);

print(set1, len(set1));


latters = set("Python");  # it covernt each character to the set
print(latters);

numbers = set([1,2,3,4,5]);  # convert the list in the set means each item in the list convert in the set
print(numbers);

# numbers = set([1,2,3], [3,4,5],[4,32,1]); it gave error becuase set only expected at most 1 argument,
print(numbers);

print(numbers, type(numbers));

# empty set
s =set() #{}
print(type(s));


set2 = {"rahul", 32, 32.4, True, 6 + 4j, 'G'}; # set are both hetrogenious and homogenious
print(set2);

a={1,2,3,4,5};
b={3,4,5,6,7,8};

#changes in original set
a.difference_update(b); # whatever the common to  both just removed and remaining a value will be printed;
print(a);
b.difference_update(a);
print(b);


print(a | b); # all the unique element of set1 and set2 will be printed ,union of the set
print(a & b); #  intersecton of the set;
print(a, b); # print a and b set sepratly in single line


a={1,2,3,4,5};
b={3,4,5,6,7,8};
a.update(b); # give the unique value from the both set i mean also give the union 
print(a);

seta = a.union(b) # a|b give the union of the both set
print(seta);
setb = a.intersection(b) # a & b give the intersection of the both set
print(setb);

setc = a.difference(b) # a-b; wahtever the uinque value in the set a is only print
print(setc);
print(a);

a={1,2,3,4,5};
b={3,4,5,6,7,8};

setf = b.difference(a) # b - a
print(setf) ;

setd = a.symmetric_difference(b) # a ^b , a-b , b-a
print(setd);

# Frozensets -its too importnat
fs = frozenset([1,2,3,5,6,7,4]);
# fs.add(10) , not possible it gave the error
print(fs)


