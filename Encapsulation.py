class Animal():
    def eat(self):
        print("Eating Eating!")

class Cat(Animal):
    __catName = ""
    def setName(self,text):
        self.catName = text
        print("Setting new Cat name =",self.catName)

    def eat(self):
        print("Meow !!", self.catName)

cat1 = Cat()
cat1.setName("MMMMM")
cat1.eat()

