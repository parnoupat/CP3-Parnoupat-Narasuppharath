amount = int(input("กรอกจำนวน * : "))
print("*"*amount)

text = ""
for i in range(amount):
    text = text+"*"
print(text)

for i in range(amount):
    i=i+1
    print("*"*i)