from tkinter import *
import tkinter
import tkinter.messagebox

mainWindow = tkinter.Tk()

mainWindow.title('Tic Tac Toe')
mainWindow.geometry('1350x750+0+0')
mainWindow.configure(background="#a45a52")

#
topFrame = tkinter.Frame(mainWindow, bg="#b9bbb6", pady=2, width=1350, height=100, relief=RIDGE)
topFrame.grid(row=0, column=0)

label = tkinter.Label(topFrame, font=('arial', 50, 'bold'), text='Tic Tac Toe', bd=21, bg="#a45a52", fg="Cornsilk", justify=CENTER)
label.grid(row=0, column=0)

mainFrame = tkinter.Frame(mainWindow, bg="#fa8072", pady=2, width=1350, height=600, relief=RIDGE)
mainFrame.grid(row=1, column=0)

leftFrame = tkinter.Frame(mainFrame, bd=10, width=750, height=500, pady=2, padx=10, bg="#a45a52", relief=RIDGE)
leftFrame.pack(side=LEFT)

rightFrame = tkinter.Frame(mainFrame, bd=10, width=560, height=500, pady=2, padx=10, bg="#a45a52", relief=RIDGE)
rightFrame.pack(side=RIGHT)

rightFrame1 = tkinter.Frame(rightFrame, bd=10, width=560, height=200, pady=2, padx=10, bg="#a45a52", relief=RIDGE)
rightFrame1.grid(row=0, column=0)

rightFrame2 = tkinter.Frame(rightFrame, bd=10, width=560, height=200, pady=2, padx=10, bg="#a45a52", relief=RIDGE)
rightFrame2.grid(row=1, column=0)

PlayerX = IntVar()
PlayerO = IntVar()

PlayerX.set(0)
PlayerO.set(0)

buttons = StringVar()
btn_click = True


def checker(button):
    global btn_click
    if button['text'] == "" and btn_click:
        button['text'] = "X"
        btn_click = False
        scorekeeper()
    elif button['text'] == "" and not btn_click:
        button['text'] = "O"
        btn_click = True
        scorekeeper()


def reset():
    button1['text'] = ""
    button2['text'] = ""
    button3['text'] = ""
    button4['text'] = ""
    button5['text'] = ""
    button6['text'] = ""
    button7['text'] = ""
    button8['text'] = ""
    button9['text'] = ""

    button1.configure(background='gainsboro')
    button2.configure(background='gainsboro')
    button3.configure(background='gainsboro')
    button4.configure(background='gainsboro')
    button5.configure(background='gainsboro')
    button6.configure(background='gainsboro')
    button7.configure(background='gainsboro')
    button8.configure(background='gainsboro')
    button9.configure(background='gainsboro')


def newGame():
    reset()
    PlayerX.set(0)
    PlayerO.set(0)


def btnX(x, y, z):
    if x['text'] == "X" and y['text'] == "X" and z['text'] == "X":
        x.configure(background='Teal')
        y.configure(background='Teal')
        z.configure(background='Teal')
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "You have just won")
        reset()


def btnO(x, y, z):
    if x['text'] == "O" and y['text'] == "O" and z['text'] == "O":
        x.configure(background='Red')
        y.configure(background='Red')
        z.configure(background='Red')
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "You have just won")
        reset()


def scorekeeper():
    btnX(button1, button2, button3)
    btnX(button4, button5, button6)
    btnX(button7, button8, button9)
    btnX(button1, button5, button9)
    btnX(button3, button5, button7)
    btnX(button1, button4, button7)
    btnX(button2, button5, button8)
    btnX(button3, button6, button9)

    btnO(button1, button2, button3)
    btnO(button4, button5, button6)
    btnO(button7, button8, button9)
    btnO(button1, button5, button9)
    btnO(button3, button5, button7)
    btnO(button1, button4, button7)
    btnO(button2, button5, button8)
    btnO(button3, button6, button9)


labelButtonX = tkinter.Label(rightFrame1, font=('arial', 40, 'bold'), text='Player X :', padx=2, pady=2, bg="#a45a52")
labelButtonX.grid(row=0, column=0, sticky=W)
textPlayerX = Entry(rightFrame1, font=('arial', 40, 'bold'), bd=2, fg='black', textvariable=PlayerX, width=14,
                    justify=LEFT).grid(row=0, column=1)

labelButtonO = tkinter.Label(rightFrame1, font=('arial', 40, 'bold'), text='Player O :', padx=2, pady=2, bg="#a45a52")
labelButtonO.grid(row=1, column=0, sticky=W)
textPlayerO = Entry(rightFrame1, font=('arial', 40, 'bold'), bd=2, fg='black', textvariable=PlayerO, width=14,
                    justify=LEFT).grid(row=1, column=1)

buttonReset = Button(rightFrame2, text="Reset", font=('arial', 40, 'bold'), height=1, width=20, command=lambda: reset())
buttonReset.grid(row=0, column=0, padx=6, pady=11)

buttonNG = Button(rightFrame2, text="New Game", font=('arial', 40, 'bold'), height=1, width=20, command=lambda: newGame())
buttonNG.grid(row=1, column=0, padx=6, pady=10)

button1 = Button(leftFrame, text="", font="Times 26 bold", height=3, width=8, bg="gainsboro", command=lambda: checker(button1))
button1.grid(row=1, column=0, sticky=S+N+E+W)

button2 = Button(leftFrame, text="", font="Times 26 bold", height=3, width=8, bg="gainsboro", command=lambda: checker(button2))
button2.grid(row=1, column=1, sticky=S+N+E+W)

button3 = Button(leftFrame, text="", font="Times 26 bold", height=3, width=8, bg="gainsboro", command=lambda: checker(button3))
button3.grid(row=1, column=2, sticky=S+N+E+W)

button4 = Button(leftFrame, text="", font="Times 26 bold", height=3, width=8, bg="gainsboro", command=lambda: checker(button4))
button4.grid(row=2, column=0, sticky=S+N+E+W)

button5 = Button(leftFrame, text="", font="Times 26 bold", height=3, width=8, bg="gainsboro", command=lambda: checker(button5))
button5.grid(row=2, column=1, sticky=S+N+E+W)

button6 = Button(leftFrame, text="", font="Times 26 bold", height=3, width=8, bg="gainsboro", command=lambda: checker(button6))
button6.grid(row=2, column=2, sticky=S+N+E+W)

button7 = Button(leftFrame, text="", font="Times 26 bold", height=3, width=8, bg="gainsboro", command=lambda: checker(button7))
button7.grid(row=3, column=0, sticky=S+N+E+W)

button8 = Button(leftFrame, text="", font="Times 26 bold", height=3, width=8, bg="gainsboro", command=lambda: checker(button8))
button8.grid(row=3, column=1, sticky=S+N+E+W)

button9 = Button(leftFrame, text="", font="Times 26 bold", height=3, width=8, bg="gainsboro", command=lambda: checker(button9))
button9.grid(row=3, column=2, sticky=S+N+E+W)

# canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=1)
# canvas.grid(row=1, column=0)


mainWindow.mainloop()

