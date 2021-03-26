menuList = []
priceList = []
def showBill():
    print(" My Food ".center(25,"-"))
    for i in range(len(menuList)):
        print(menuList[i],priceList[i])
def totalPrice():
    print(" Total ".center(25,"-"))
    totalPrice = 0
    for i in range(len(priceList)):
        totalPrice += int(priceList[i])
    return totalPrice
while True:
    menuName = input("ชื่อสินค้า : ")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = input("ราคาสินค้า : ")
        menuList.append(menuName)
        priceList.append(menuPrice)
showBill()
print(totalPrice(),"THB")
