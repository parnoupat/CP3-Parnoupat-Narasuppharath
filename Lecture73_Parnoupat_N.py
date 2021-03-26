
systemMenu = {"ข้าวหมกไก่":45,"ข้าวมันไก่":40,"ข้าวมันไก่ปสม":50,"ข้าวมันไก่พิเศษ":45}


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
        menuList.append([menuName,systemMenu[menuName]])
showBill()
print(totalPrice(),"THB")
