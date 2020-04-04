# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 12:09:10 2020

@author: Tyson
"""

from tkinter import *
import tkinter.messagebox

window = Tk()
window.title("Tic Tac Toe")
turn = "X"
total_turns=0
p1 = StringVar()
p2 = StringVar()


player1_name = Entry(window,textvariable = p1,bd=5)
player1_name.grid(row=1,column=1,columnspan=8)
player2_name = Entry(window,textvariable = p2,bd=5)
player2_name.grid(row=2,column=1,columnspan=8)

def disableButton():
    button1.configure(state = DISABLED)
    button2.configure(state = DISABLED)
    button3.configure(state = DISABLED)
    button4.configure(state = DISABLED)
    button5.configure(state = DISABLED)
    button6.configure(state = DISABLED)
    button7.configure(state = DISABLED)
    button8.configure(state = DISABLED)
    button9.configure(state = DISABLED)

def checkForWin():
    if (button1["text"]=="X" and button2["text"]=="X" and button3["text"]=="X" or
        button4["text"]=="X" and button5["text"]=="X" and button6["text"]=="X" or
        button7["text"]=="X" and button8["text"]=="X" and button9["text"]=="X" or
        button1["text"]=="X" and button4["text"]=="X" and button7["text"]=="X" or
        button2["text"]=="X" and button5["text"]=="X" and button8["text"]=="X" or
        button3["text"]=="X" and button6["text"]=="X" and button9["text"]=="X" or
        button1["text"]=="X" and button5["text"]=="X" and button9["text"]=="X" or
        button7["text"]=="X" and button5["text"]=="X" and button3["text"]=="X" ):
            pa = p1.get()+" wins!!!"
            disableButton()
            tkinter.messagebox.showinfo("Tic tac toe",pa)
            
    elif (button1["text"]=="O" and button2["text"]=="O" and button3["text"]=="O" or
        button4["text"]=="O" and button5["text"]=="O" and button6["text"]=="O" or
        button7["text"]=="O" and button8["text"]=="O" and button9["text"]=="O" or
        button1["text"]=="O" and button4["text"]=="O" and button7["text"]=="O" or
        button2["text"]=="O" and button5["text"]=="O" and button8["text"]=="O" or
        button3["text"]=="O" and button6["text"]=="O" and button9["text"]=="O" or
        button1["text"]=="O" and button5["text"]=="O" and button9["text"]=="O" or
        button7["text"]=="O" and button5["text"]=="O" and button3["text"]=="O" ):
            disableButton()
            pb = p2.get()+" wins!!!"
            tkinter.messagebox.showinfo("Tic tac toe",pb)
    elif total_turns==8:
        disableButton()
        tkinter.messagebox.showinfo("Tic tac toe","It is a tie")



def btnClick(button):
    global turn,total_turns,player1_name,player2_name
    if button["text"]==" " and turn=="X":
        button["text"]=turn
        turn = "O"
        checkForWin()
        total_turns = total_turns+1
    elif button["text"]==" " and turn=="O":
        button["text"]=turn
        turn = "X"
        checkForWin()
        total_turns = total_turns+1
        
    else:
        tkinter.messagebox.showinfo("Tic tac toe","Button already clicked")
        



label1 = Label(window, text="Player 1:", font="Times 20 bold" ,bg="white",fg="black",height=1,width=8 )
label1.grid(row=1, column=0)

label2 = Label(window, text="Player 2:", font="Times 20 bold" ,bg="white",fg="black",height=1,width=8 )
label2.grid(row=2, column=0)

button1 = Button(window, text=" ", font='Times 20 bold', bg="gray", fg="white", height=4, width=8, command=lambda : btnClick(button1))
button1.grid(row=3,column=0)

button2 = Button(window, text=" ", font='Times 20 bold', bg="gray", fg="white", height=4, width=8, command=lambda : btnClick(button2))
button2.grid(row=3,column=1)

button3 = Button(window, text=" ", font='Times 20 bold', bg="gray", fg="white", height=4, width=8, command=lambda : btnClick(button3))
button3.grid(row=3,column=2)

button4 = Button(window, text=" ", font='Times 20 bold', bg="gray", fg="white", height=4, width=8, command=lambda : btnClick(button4))
button4.grid(row=4,column=0)

button5 = Button(window, text=" ", font='Times 20 bold', bg="gray", fg="white", height=4, width=8, command=lambda : btnClick(button5))
button5.grid(row=4,column=1)

button6 = Button(window, text=" ", font='Times 20 bold', bg="gray", fg="white", height=4, width=8, command=lambda : btnClick(button6))
button6.grid(row=4,column=2)

button7 = Button(window, text=" ", font='Times 20 bold', bg="gray", fg="white", height=4, width=8, command=lambda : btnClick(button7))
button7.grid(row=5,column=0)

button8 = Button(window, text=" ", font='Times 20 bold', bg="gray", fg="white", height=4, width=8, command=lambda : btnClick(button8))
button8.grid(row=5,column=1)

button9 = Button(window, text=" ", font='Times 20 bold', bg="gray", fg="white", height=4, width=8, command=lambda : btnClick(button9))
button9.grid(row=5,column=2)



window.mainloop()