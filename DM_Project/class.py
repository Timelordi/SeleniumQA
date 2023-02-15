class MyClass:
    name = None
    age = None
    isHappy = None
    tail = True

    def __init__(self,name, age, isHappy, tail = None):
        self.name = name
        self.age = age
        self.isHappy = isHappy
        self.tail = tail


    def set_data(self, name, age, isHappy, tail = None):
        self.set_data(name, age, isHappy, tail)
        self.get_data()

    def get_data(self):
        print(self.name, "Age: ", self.age, "Is it happy: ", self.isHappy, " Tail: ", self.tail)

cat1 = my_class("Tuzik", 9, True, True)
#cat1.set_data("Tuzik", 9, True, True)

cat2 = my_class("Bober", 7, False, False)
#cat2.set_data("Bober", 7, False, False)


cat3 = my_class("Barsik",  5, True)

cat1.get_data()
cat2.get_data()
cat3.get_data()
