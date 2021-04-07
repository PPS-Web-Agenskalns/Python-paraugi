from tkinter import *
logs = Tk()
logs.geometry("400x500")

C = 0

def pieskaitit():
    global C
    C = C+1
    skaititajs.config(text = C)

    poga1.config(text = ievade.get())
    ievade.delete(0, END)

    


poga1 = Button(logs, text = "MANA PRIMA POGA",
               fg = "red",
               bg = "yellow",
               font = "50",
               command=pieskaitit)
poga1.place(x = 200, y = 250)

skaititajs = Label(logs, fg = "green",
                   text = "0",
                   font="Arial 100")
skaititajs.place(x = 100, y = 20)

ievade = Entry(logs, width="20")
ievade.place(x = 200, y = 300)

