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
    
    ievade = skaititajs.cget("text")

    izvade = 0
    summa = 0
    irMinuss = False
    irReiz = False
    irDal = False

    List = []

    for c in ievade:
        asci = ord(c)
    
        if asci<=57 and asci>=48:
            skaitlis = asci - 48;
            izvade = izvade * 10 + skaitlis;
        
        
        else:
        

            if irMinuss == True:
                izvade = izvade * -1 
                irMinuss = False

            if c == '-':
                irMinuss = True

            if irReiz == True:
                izvade = izvade * List.pop()
                irReiz = False

            if c == '*':
                irReiz = True

            if irDal == True:
                izvade = List.pop() / izvade
                irDal = False

            if c == '/':
                irDal = True
        
            List.append(izvade)
            izvade = 0
            

    if irMinuss == True:
        izvade = izvade * -1 
        irMinuss = False

    if c == '-':
        irMinuss = True

    if irReiz == True:
        izvade = List.pop() * izvade
        irReiz = False

    if c == '*':
        irReiz = True

    if irDal == True:
        izvade = List.pop() / izvade
        irDal = False

    if c == '/':
        irDal = True
        
    List.append(izvade)
    izvade = 0

    print("summa", sum(List))
    skaititajs.config(text = str(sum(List)))






    
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

