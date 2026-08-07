class Mentor:
    name = "Gaurav Kumar";
    age = 22;
    skill = "python";

    def teach(self):
        print("I am teaching python programming language");
        print(self.name);

    def groom(self):
        print("I am grooming students for interviews");
        print(self.name);


m = Mentor();
print(f"Mentor name is: {m.name}");
print(f"Mentor age is: {m.age}");
print(f"Mentor skill is: {m.skill}");

m.teach();
m.groom();



class student:
    name = "Rohit";
    age = 21;
    skill = "java";
    state = "Bihar";

    def learn(self):
        print("I am learning java programming language");
        print(self.name);

    def practice(self):
        print("I am practicing coding questions");
        print(self.name);
        print(self.state);

    def attend(self):
        print("I am attending classes");
        print(self.name);
        print(self.state);


    def submit(self):
        print("I am submitting assignments");
        print(self.name);
        print(self.state) 


s = student();
print(f"Student name is: {s.name}");
print(f"Student age is: {s.age}");
print(f"Student skill is: {s.skill}");
s.learn();
s.practice();
s.attend();
s.submit();