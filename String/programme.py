str = "Gaurav";
print(str);

print(str[0]); # G
print(str[-0]); # G
print(str[-1]); # v

print(id(str));  # give the address of the variable in memory


# STRING SLICING
str = "Gaurav";
print(str[0:4]); # Gaur

print(len(str)); # 6
print(str[0:len(str)]); # Gaurav
print(str[2:]); # urav
print(str[:4]); # Gaur
print(str[:]); # Gaurav

print(str[-3:-1]); # ra
print(str[-7:-1]); # Gaurav  because -7 is out of range so it will start from 0 index
print(str[-7:]); # Gaurav  because -7 is out of range so it will start from 0 index
print(str[: -3]); # Gau 
print(str[2:3]); # u
print(str[2:2]); # empty string

# STRING SLICING WITH STEP
# if we want to skip some characters then we can use step in slicing
str = "VISHWAKARMA";
print(str[0:10:2]); # VSWKRM
print(str[0:10:3]); # VHKM
print(str[::2]); # VSWKRM

# STRING SLICING WITH NEGATIVE STEP 
# if start index is greater than end index then we can use negative step
str = "VISHWAKARMA";
print(str[::-1]); # AMRAKAWHSIV
print(str[0:6:-1]); # not working
print(str[4:0:-1]); # WHSI
print(str[3:6:-1]); # now working
print(str[: : -1]); # AMRAKAWHSIV
print(str[6: :]); # KARMA
print(str[6: : -1]); # KAWHSIV
print(str[: : -2]); # MRAKAWHIV



#   STRING METHODS 

str = " Kodnest Technologies 123 ";

print("Original String:", str);

# case conversion methods
print("Upper Case:", str.upper()); # KODNEST TECHNOLOGIES 123
print("Lower Case:", str.lower()); # kodnest technologies 123
print("Title Case:", str.title()); # Kodnest Technologies 123 , each word's first character is converted to the uppercase;
print("Capitalize:", str.capitalize()); # Kodnest technologies 123 , only the first character of the string is converted to the upper case;
print("Swap Case:", str.swapcase()); # kODNEST tECHNOLOGIES 123 , all the upper case characters are converted to lower case and vice versa;

#Searching & counting methods
print("Count of 'e':", str.count('e')); # 2
print("find('Tech'):", str.find('Tech')); # 6

#Replace
print("Replace 'Technologies' with 'Institute':", str.replace('Technologies', 'Institute')); # Kodnest Institute 123

#Start and End with
print("Starts with 'K':", str.startswith('K')); # True
print("Ends with '3':", str.endswith('3')); # True

#Split & Join
print("Split:", str.split()); # ['Kodnest', 'Technologies', '123']
print("Join:", '-'.join(str.split())); # Kodnest-Techonologies-123;


#Strip space
print("Original String:", str);
print("Strip:", str.strip()); # Kodnest Technologies 123, Strip method removes the leading and trailing spaces from the string;

#Checking methods
print("Is alphanumeric:", str.isalnum()); # False
print("Is alphabetic:", str.isalpha()); # False
print("Is digit:", str.isdigit()); # False

#Length of the string
print("Length of the string:", len(str)); # 24