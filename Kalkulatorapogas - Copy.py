from tkinter import *

logs = Tk()
logs.geometry("400x500")


def viens():
    skaititajs.config(text = str(skaititajs.cget("text")) + '1')
def divi():
    skaititajs.config(text = str(skaititajs.cget("text")) + '2')
def plus():
    skaititajs.config(text = str(skaititajs.cget("text")) + '+')

def delete():
    skaititajs.config(text = str(skaititajs.cget("text")[:-1]))

def rez():
    ievade = str(skaititajs.cget("text"))

    cip = 0
    summa = 0
    irNegativs = False

    for c in ievade:
        if ord(c)>=48 and ord(c)<=57:
           cip = cip * 10
           cip = cip + (ord(c)-48)

        else:
        
            
            if irNegativs == True:
                irNegativs = False
                cip = cip * -1

            if c == '-':
                irNegativs = True
        
        

            print(cip)
            summa = summa + cip
            print("summa: ", summa)
            cip = 0

    print(cip)
    summa = summa + cip
    print("summa: ", summa)
    skaititajs.config(text = summa)




    
poga1 = Button(logs, bg = "red", fg = "green",
               font = "Arial 30", text = 1,
               command = viens)
poga1.place(x = 90,y = 400)

dzest = Button(logs, bg = "red", fg = "green",
               font = "Arial 30", text = "<---",
               command = delete)
dzest.place(x = 90,y = 100)

poga2 = Button(logs, bg = "red", fg = "green",
               font = "Arial 30", text = 2,
               command = divi)
poga2.place(x = 150,y = 400)

pogaP = Button(logs, bg = "red", fg = "green",
               font = "Arial 30", text = "+",
               command = plus)
pogaP.place(x = 210, y = 400)

pogaP = Button(logs, bg = "red", fg = "green",
               font = "Arial 30", text = "=",
               command = rez)
pogaP.place(x = 270, y = 400)


skaititajs = Label(logs, text = "", font = "Arial 20")
skaititajs.place(x = 90, y =300)

