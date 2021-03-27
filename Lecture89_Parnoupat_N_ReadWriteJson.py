import json
file = open("demo.txt", "r")

print(file.readline())
print(file.read(10))
print(file.read())

def createTxt():
    file = open("demo1.txt", "x")
    file.write("Haha From Next Lecture")


def writeJson():
    n = input("พิมพ์ชื่อ file : ")
    # สร้างข้อมูลที่เราต้องการแปลง(ประเภท dictionary)
    x = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    # คำสั่งที่ใช้ในการแปลง
    y = json.dumps(x)
    # มาลองดูผลลัพธ์กัน
    # print(y)
    file = open(n+".json", "x")
    file.write(y)

# writeJson()

def readJson(n,m):
    file = open(n+".json", "r")
    x = file.read()
    # ข้อมูล JSON ที่เราต้องการอ่าน
    # x =  '{ "name":"John", "age":30, "city":"New York"}'
    # แปลงข้อมูลให้กลายเป็นรูปที่เราสามารถใช้ได้
    y = json.loads(x)
    # ทำการเรียกข้อมูล age ออกมาแสดง
    print(y[m])
# readJson()
readJson("testexportjson","name")