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
    if selectOther == "N" or selectOther == "n" :
        totalprice = price1 * amount1
        print("ราคาที่ท่านต้องจ่ายคือ : ",totalprice," THB")
    elif selectOther == "Y" or selectOther == "y":
        print("----- เลือกสินค้าเพิ่มเติม -----")
        print("1. Pen --------------- ", pen, " THB")
        print("2. Ruler ------------- ", ruler, " THB")
        print("3. Paper ------------- ", paper, " THB")
        print("4. Rubber ------------ ", rubber, " THB")
        print("5. Pencil ------------ ", pencil, " THB")
        userSelected2 = int(input("กรุณาเลือกสินค้าอีก 1 อย่าง >> "))
        if userSelected2 == 1:
            selected2 = "pen"
        elif userSelected2 == 2:
            selected2 = "Ruler"
        elif userSelected2 == 3:
            selected2 = "Paper"
        elif userSelected2 == 4:
            selected2 = "Rubber"
        elif userSelected2 == 5:
            selected2 = "Pencil"
        amount2 = int(input("ใส่จำนวน " + selected2 + " ที่ท่านต้องการ >> "))
        if userSelected2 == 1:
            price2 = pen
        elif userSelected2 == 2:
            price2 = ruler
        elif userSelected2 == 3:
            price2 = paper
        elif userSelected2 == 4:
            price2 = rubber
        elif userSelected2 == 5:
            price2 = pencil
        totalprice = (price1 * amount1)+(price2 * amount2)
        print(selected," ราคา ", price1 ," ซื้อ ", amount1 , "ชิ้น เป็นเงิน : ", (price1 * amount1))
        print(selected2 , " ราคา " , price2 , " ซื้อ " , amount2 , "ชิ้น เป็นเงิน : " , (price2 * amount2))
        print("================ Total =================")
        print("ราคาที่ท่านต้องจ่ายคือ : ", totalprice, " THB")
    print("***************************************")
    print("ขอบคุณที่ใช้บริการ ^^")



elif passwordInput != "1234" :
    print("Wrong Password !!!!!!")
else :
    print("Wrong")
