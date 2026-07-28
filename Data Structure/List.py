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



#membership operator

number =[2,4,1,9,3];
print(2 in number);
print(33 in number);


# read item ine by one 
color  = ["Green","Red","pink","yellow"];
for c in color:
    print(c);

favcolor = color.copy();# use of this we can copy the original list and store in th other variable
print(favcolor);

#print the length of the string
print(len(favcolor));
print(max(number)); # give the max value of the list
print(min(number)); # give the min value of the list
print(max(color)); # for the string it give the value using the laxcographically order
print(sum(number)) # give the sum of all the items

new_num = number.copy();
print(new_num)
new_num.sort(); # sort the number in the assending order 
print(new_num)
new_num.reverse(); # sort the number or list item in decending order
print(new_num)

new_num.sort(reverse=True); # also use to rever (decending order) of the list
print(new_num)


#append the two or more list
list1 = [2,3,4];
list2 = [5,6,7];
new_list = list1 + list2;
print(new_list);
new_list = list2.extend(list1);
print(new_list);


print(color.index("yellow"));
print(color.count("red"));

#split splite the word and pring the list of the word
words = input().split();
print(words);

#list in list
list_in_list = [["Gaurav" ,22 ,"Rewa"], ["Rahul",32 ,"Bharuch"],["priya",32,"Uttar Pradesh"]];
print(list_in_list);
for i in list_in_list:
    print(i);

