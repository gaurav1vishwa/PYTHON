# one Child class and multiple parents class

class Father:
    def skills(self):
        return "Gardening, Programming"


class Mother:
    def skills(self):
        return "Cooking, Art"


class Child(Father, Mother):
    pass

c = Child()
print(c.skills()) # Gardening (Father comes first in MRO, so Father's skills method is called)