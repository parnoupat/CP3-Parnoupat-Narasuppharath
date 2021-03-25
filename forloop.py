inputRound = int(input("Please Enter Number : "))
sum = 0
for x in range(inputRound):
    inputNumber = int(input("x"+str(x+1)+" : "))
    sum += inputNumber
print(sum)