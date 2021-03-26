
menuList = []
def showBill():
    print(" My Food ".center(25,"-"))
    for i in range(len(menuList)):
        print(menuList[i][0],menuList[i][1])
def totalPrice():
    print(" Total ".center(25,"-"))
    totalPrice = 0
    for i in range(len(menuList)):
        totalPrice += int(menuList[i][1])
    return totalPrice
while True:
    menuName = input("ชื่อสินค้า : ")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = input("ราคาสินค้า : ")
        menuList.append([menuName,menuPrice])
showBill()
print(totalPrice(),"THB")
