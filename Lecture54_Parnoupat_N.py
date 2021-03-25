def login():
    usernameInput = input("Username :")
    passwordInput = input("Password :")
    if usernameInput == "admin" and passwordInput == "1234":
        return True
    else:
        return False
def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
def menuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1:
        vatResult = vatCalculator(int(input("Price (THB) : ")))
        print(vatResult)
    elif userSelected == 2:
        print(priceCalculate())
def vatCalculator(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result
def priceCalculate():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculator(price1 + price2)

if login():
    showMenu()
    menuSelect()
else:
    print("Wrong User or Password")