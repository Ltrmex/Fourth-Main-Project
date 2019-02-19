from tkinter import *

window = Tk()
window.title("Fourth Year Main Assignment")
window.configure(width=500, height=500, bg="black")

Label(text="Google AIY v/s Our Code", bg="blue", fg="white", font=("Helvetica", 16)).pack(fill=X)

frame = Frame(width=250, bd=5, relief=SUNKEN, bg="red")
frame.pack(side = LEFT, fill=Y, padx=5, pady=5)
frame2 = Frame(width=250, bd=5, relief=SUNKEN, bg="red")
frame2.pack(side = RIGHT, fill=Y, padx=5, pady=5)

Label(frame, text="Google AIY", bg="black", fg="white", font=("Helvetica", 12)).pack(fill=X)
Label(frame2, text="Our Code", bg="black", fg="white", font=("Helvetica", 12)).pack(fill=X)

photo2 = PhotoImage(file="C:/Users/Ltrmex/Desktop/Fourth-Main-Project/Code/GUI/Images/GoogleAIY.png")
Label(frame, image=photo2).pack()
photo = PhotoImage(file="C:/Users/Ltrmex/Desktop/Fourth-Main-Project/Code/GUI/Images/Python.png")
Label(frame2, image=photo).pack()

window.mainloop()