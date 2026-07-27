fruit_list = ["banana","Guava","papaya","grapes"];
print(fruit_list);  # order collecton of items

# list if collection of hetrogenious and homogenious 
# homogenious - same data type
# hetrogenious - difference data type 

mixed = [ 1, 'a', "gaurav", True, 32.23];
print(mixed);

# getting a particluar index by list indexing number 
print(mixed[2]);
print(mixed[-1]); # it give the index value at the end -1 means starting index with the reverse order

# mutablity and immutable - list is mutable

fruit_list = ["banana","Guava","papaya","grapes","mango"];
fruit_list[1]="orange"; # modified the list by inder the new value and replate it with the new one 
print(fruit_list);


# adding the item in the list
fruit_list.append("dragon fruit"); # its append the value or the item at the end of the list
print(fruit_list)
# add the item at the specif index
fruit_list.insert(1,"pineapple");
print(fruit_list);


#Delete the item at the particular index
del fruit_list[0];
print(fruit_list);
# we can also delete the itme by there name 
fruit_list.remove("orange");
print(fruit_list);
# we can also delete the item at the end of the list
fruit_list.pop();
print(fruit_list);
# we can also delete the all itme from the list
fruit_list.clear();
print(fruit_list); # empty list
