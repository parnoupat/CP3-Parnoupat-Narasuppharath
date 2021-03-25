for i in range(12):
    i=i+1
    for x in range(12):
        x = x+1
        y = i*x
        print(str(i) + " x " + str(x) + " = " + str(y))
    print("--------------------------")


for val in "hello":
    if val == "l":
        continue
    print(val)