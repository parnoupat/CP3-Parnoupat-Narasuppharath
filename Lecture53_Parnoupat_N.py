def vatCalculate(totalPrice):
    result = totalPrice*107/100
    return result

print(vatCalculate(int(input("กรอกราคาที่ต้องการคำนวนภาษี :"))))