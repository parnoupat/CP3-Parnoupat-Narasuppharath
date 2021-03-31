class Animal:
    def eat(self):
        print("Eating Eating!")

class Cat(Animal):
    def eat(self):
        print("Meaw Meaw")

cat1 = Cat()
cat1.eat()