from tkinter import  *
from random import *

koloda = [2,3,4,5,6,7,8,9,10,'Валет', 'Дама', 'Король', 'Туз'] * 4

shuffle(koloda)

count = 0

def take():
    global count, koloda

    karta = koloda.pop()

    if karta=='Валет' or karta=='Дама' or karta=='Король':
        karta=10

    if karta=='Туз':
        karta=11

    count += karta

    if count>21:
        text3["text"] = 'Вы проиграли, у вас '+ str(count) +'очков'
        text2["text"] = 'Вы проиграли'
    else:
        text2["text"] = "У вас" + str(count)+ "очков"

def enough():
    global count

    if count == 21:
        text3["text"]='Поздравляем, у вас 21'

    if count < 21:
        text3["text"]='У вас ' + str(count) + 'очков'

root = Tk()
root.geometry("300x140")

text1 = Label(root, text="Игра в Black-Jack", fg="red")
text1.place(x=100,y=0)

text2 = Label(root, text="У вас 0 очков", fg="blue")
text2.place(x=110,y=30)

but1 = Button(root, width="15", text="Взять карту", command=take)
but1.place(x=20,y=60)

but1 = Button(root, width="15", text="Хватит", command=enough)
but1.place(x=160, y=60)

text3 = Label(root, text="Результат игры", fg="red")
text3.place(x=90,y=100)

root.mainloop()