class Building:
    year = None
    city = None

    def __init__(self, year, city):
        self.year = year
        self.city = city

    def get_info(self):
        print("Year: ", self.year, "City: ", self.city)

class School(Building):
    pupils = 0

    def __init__(self, year, city, pupils):
        self.pupils = pupils
        super(School,self).__init__(year, city)

    def get_info(self):
        print(super().get_info(), " Pupils: ", self.pupils)

class House(Building):
    pass

class Shop(Building):
    pass

school = School(2000, "Kharkiv", 1000)
house = House(1991, "Donetsk")
shop = Shop(1999, "Msida")

print(school.get_info())