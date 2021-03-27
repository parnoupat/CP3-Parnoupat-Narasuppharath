from tkinter import *

def clickResult(event):
    labelResult.configure(text=BMICal())
    labelResultTrans.configure(text=BMITrans())
def BMICal():
    w = float(textBoxWeight.get())
    h = float(textBoxHeight.get())/100
    bmi = round(w/h/h,2)
    return bmi
def BMITrans():
    bmi = BMICal()
    if bmi <= 18.50:
        bmiTrans = "อยู่ในเกณฑ์น้ำหนักน้อย / ผอม"
    elif bmi <= 22.90:
        bmiTrans = "อยู่ในเกณฑ์ปกติ (สุขภาพดี)"
    elif bmi <= 24.90:
        bmiTrans = "อยู่ในเกณฑ์ท้วม / โรคอ้วนระดับ 1"
    elif bmi <= 29.90:
        bmiTrans = "อยู่ในเกณฑ์อ้วน / โรคอ้วนระดับ 2"
    elif bmi > 29.90:
        bmiTrans = "อยู่ในเกณฑ์อ้วนมาก / โรคอ้วนระดับ 3"
    return bmiTrans

MainWindow = Tk()
labelHeight = Label(MainWindow, text="ส่วนสูง (cm.)")
labelHeight.grid(row=0,column=0)

textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)

labelWeigth = Label(MainWindow, text="น้ำหนัก (Kg.)")
labelWeigth.grid(row=1,column=0)

textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)

labelTextResult = Label(MainWindow, text="BMI ของท่านคือ :")
labelTextResult.grid(row=3, column=0)

labelResult = Label(MainWindow, text="")
labelResult.grid(row=3, column=1)

labelResultTrans = Label(MainWindow, text="")
labelResultTrans.grid(row=4)

calculateButton = Button(MainWindow,text = "คำนวน")
calculateButton.grid(row=2)
calculateButton.bind('<Button-1>',clickResult)

MainWindow.mainloop()