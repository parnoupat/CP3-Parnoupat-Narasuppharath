usernameInput = input("Username :")
passwordInput = input("Password :")
if usernameInput == "admin" and passwordInput == "1234":
    print("Done !")
    pen = 10
    ruler = 12
    paper = 2
    rubber = 20
    pencil = 12
    print("----- Parnoupat's Shop -----")
    print("1. Pen --------------- ",pen," THB")
    print("2. Ruler ------------- ",ruler," THB")
    print("3. Paper ------------- ",paper," THB")
    print("4. Rubber ------------ ",rubber," THB")
    print("5. Pencil ------------ ",pencil," THB")

    userSelected1 = int(input("กรุณาเลือกสินค้า 1 อย่าง >> "))
    if userSelected1 == 1:
        selected = "pen"
    elif userSelected1 == 2:
        selected = "Ruler"
    elif userSelected1 == 3:
        selected = "Paper"
    elif userSelected1 == 4:
        selected = "Rubber"
    elif userSelected1 == 5:
        selected = "Pencil"
    amount1 = int(input("ใส่จำนวน "+selected+" ที่ท่านต้องการ >> "))
    price1 = 0
    if userSelected1 == 1:
        price1 = pen
    elif userSelected1 == 2:
        price1 = ruler
    elif userSelected1 == 3:
        price1 = paper
    elif userSelected1 == 4:
        price1 = rubber
    elif userSelected1 == 5:
        price1 = pencil
    print("ท่านต้องการเลือกของอย่างอื่นอีกหรือไม่")
    print("Y ต้องการ")
    print("N ไม่ต้องการ")
    selectOther = input(">> ")
    if selectOther == "N":
        totalprice = price1 * amount1
        print("ราคาที่ท่านต้องจ่ายคือ : ",totalprice)



    # vat = 7
    # result = price + (price * 7 / 100)
    # print(result)
    # elif userSelected == 2:
    #     price1 = int(input("First Product Price : "))
    #     price2 = int(input("Second Product Price : "))
    #     print(price1+price2)
elif passwordInput != "1234" :
    print("Wrong Password !!!!!!")
else :
    print("Wrong")
