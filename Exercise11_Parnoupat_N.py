
height = int(input("ความสูงของพีรามิด : "))

for i in range(height):
    space = height - i - 1
    i=2*i+1
    print(" "*space + "*"*i + " "*space )

    # "   *   " แถวที่ 0 ว่าง 3  * 1
    # "  ***  " แถวที่ 1 ว่าง 2  * 3
    # " ***** " แถวที่ 2 ว่าง 1  * 5
    # "*******" แถวที่ 3 ว่าง 0  * 7