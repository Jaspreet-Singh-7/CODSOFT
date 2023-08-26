from tkinter import *

win = Tk()

def delete():
    mylist.delete(ANCHOR)

def add():
    mylist.insert(END, myentry.get())
    myentry.delete(0,END)

fr = Frame(win,bg="lightblue",width=100)
fr.pack(pady=10)

lab = Label(fr,text="ToDo List",font=("helvetica",30),bg="lightblue")
lab.pack(pady=10)

entryframe = Frame(win)
entryframe.pack(pady=10)

myentry = Entry(entryframe,text="Add Items",font=("Vista",24))
myentry.pack(pady=20)

buttonframe = Frame(win)
buttonframe.pack(pady=20)

delete = Button(buttonframe,text="Delete",borderwidth=0,font=("helvetica",20),bg="red",command=delete)
delete.grid(row=0,column=0)

myframe = Frame(win)
myframe.pack(pady=10)

mylist = Listbox(myframe,font=("Vista",24),width=25,height=5,bg="SystemButtonFace",bd=0,fg="#464646",highlightthickness=0,selectbackground="#a6a6a6",activestyle="none")
mylist.pack()

add = Button(buttonframe,text="Add",borderwidth=0,font=("helvetica",20),bg="#00ff00",command=add)
add.grid(row=0,column=2)

win.mainloop()