from tkinter import *

logs = Tk()
logs.geometry("400x500")


def viens():
    skaititajs.config(text = str(skaititajs.cget("text")) + '1')

def divi():
    skaititajs.config(text = str(skaititajs.cget("text")) + '2')




    
poga1 = Button(logs, bg = "red", fg = "green",
               font = "Arial 30", text = 1,
               command = viens)
poga1.place(x = 90,y = 400)

poga2 = Button(logs, bg = "red", fg = "green",
               font = "Arial 30", text = 2,
               command = divi)
poga2.place(x = 150,y = 400)

skaititajs = Label(logs, text = 0, font = "Arial 20")
skaititajs.place(x = 90, y =300)

