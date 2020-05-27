from tkinter import *

root = Tk()

def myclick():
    myLabel = Label(root,text = "clicked!")
    myLabel.pack()

mybutton = Button(root,text = "try click",command = myclick,padx = 10 , pady =10)
#other parameters state = DISABLED ,fg = "<color>" ,bg = "<color>""

mybutton.pack()

root.mainloop()