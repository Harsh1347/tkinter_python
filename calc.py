from tkinter import *

root = Tk()
#adding title
root.title("Python Calc")
#creating input box
e = Entry(root,width = 35, borderwidth = 5)
e.grid(row = 0,column = 0,columnspan = 3,padx = 10,pady=10)

def click(num):
    curr = e.get()
    e.delete(0,END)
    e.insert(0,curr +str(num))

def clear():
    e.delete(0,END) 

def b_add():
    first_num = e.get()
    global fnum 
    global maths
    maths = 'add'
    fnum = int(first_num)
    e.delete(0,END)

def b_sub():
    first_num = e.get()
    global fnum 
    global maths
    maths = 'sub'
    fnum = int(first_num)
    e.delete(0,END)

def b_mul():
    first_num = e.get()
    global fnum 
    global maths
    maths = 'mul'
    fnum = int(first_num)
    e.delete(0,END)

def b_div():
    first_num = e.get()
    global fnum 
    global maths
    maths = 'div'
    fnum = int(first_num)
    e.delete(0,END)


def eq():
    second_num = e.get()
    e.delete(0,END)
    if maths == 'add':
        e.insert(0,fnum + int(second_num))
    if maths == 'sub':
        e.insert(0,fnum - int(second_num))
    if maths == 'mul':
        e.insert(0,fnum * int(second_num))
    if maths == 'div':
        e.insert(0,fnum / int(second_num))
    
#defining buttons
button0 = Button(root,text='0',padx= 40,pady=20,command = lambda : click(0))
button1 = Button(root,text='1',padx= 40,pady=20,command = lambda : click(1))
button2 = Button(root,text='2',padx= 40,pady=20,command = lambda : click(2))
button3 = Button(root,text='3',padx= 40,pady=20,command = lambda : click(3))
button4 = Button(root,text='4',padx= 40,pady=20,command = lambda : click(4))
button5 = Button(root,text='5',padx= 40,pady=20,command = lambda : click(5))
button6 = Button(root,text='6',padx= 40,pady=20,command = lambda : click(6))
button7 = Button(root,text='7',padx= 40,pady=20,command = lambda : click(7))
button8 = Button(root,text='8',padx= 40,pady=20,command = lambda : click(8))
button9 = Button(root,text='9',padx= 40,pady=20,command = lambda : click(9))
button_add = Button(root,text = '+',padx = 39,pady = 20,command = b_add)
button_sub = Button(root,text = '-',padx = 39,pady = 20,command = b_sub)
button_mul = Button(root,text = '*',padx = 40,pady = 20,command = b_mul)
button_div = Button(root,text = '/',padx = 40,pady = 20,command = b_div)
button_eq = Button(root,text = '=',padx = 39,pady = 52,command = eq)
button_cls = Button(root,text = 'CLEAR',padx = 25,pady = 52,command = clear)


#putting buttons on grid
button_eq.grid(row =5,column =2,rowspan=2)
button_cls.grid(row =5,column =1,rowspan=2)
button_mul.grid(row=5,column=0)
button_div.grid(row=6,column=0)
button0.grid(row =4,column =2)
button_add.grid(row =4,column =0)
button_sub.grid(row =4,column =1)
button1.grid(row =3,column =0)
button2.grid(row =3,column =1)
button3.grid(row =3,column =2)
button4.grid(row =2,column =0)
button5.grid(row =2,column =1)
button6.grid(row =2,column =2)
button7.grid(row =1,column =0)
button8.grid(row =1,column =1)
button9.grid(row =1,column =2)

root.mainloop()