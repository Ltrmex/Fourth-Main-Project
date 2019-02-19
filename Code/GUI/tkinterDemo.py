from tkinter import *

window = Tk()
window.title("GUI")

#one = Label(root, text="One", bg="red", fg="white")
#one.pack()

#two = Label(root, text="Two", bg="green", fg="black")
#two.pack(fill=X)

#three = Label(root, text="Three", bg="blue", fg="white")
#three.pack(side=LEFT, fill=Y)


label1 = Label(window, text="Name", bg="red", fg="white")
label2 = Label(window, text="Password")
entry1 = Entry(window)
entry2 = Entry(window)

label1.grid(row=0, sticky=E)
label2.grid(row=1, sticky=E)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

c = Checkbutton(window, text="Keep me logged in")
c.grid(columnspan=2)

window.mainloop()