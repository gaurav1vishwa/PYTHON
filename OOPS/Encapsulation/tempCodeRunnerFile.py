class University:
    __name = "APSU";

    def get_name(self):
        print(f"the name of university is {self.__name}");

u = University();
u.get_name();