

userInput = int(input("type number of your fruit : "))
myFruits = set()
while len(myFruits) < userInput :
    myFruits.add(input("Fruit : "))
    print(myFruits)