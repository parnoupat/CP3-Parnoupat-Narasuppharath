start = int(input("Start :"))
step = int(input("Step :"))
result = ""
for i in range(5):
    # print(start + step*i, end="bb")
    result += str(start + step * i + 1)
print(result)
