from tkinter import *

root = Tk()

inp = Entry(root,width = 50,borderwidth = 5) # other parameters include color
inp.pack()
inp.insert(0,'please enter your name')
def myclick():
    myLabel = Label(root,text = inp.get())
    myLabel.pack()

mybutton = Button(root,text = "enter name",command = myclick,padx = 10 , pady =10)
#other parameters state = DISABLED ,fg = "<color>" ,bg = "<color>""

mybutton.pack()

root.mainloop()