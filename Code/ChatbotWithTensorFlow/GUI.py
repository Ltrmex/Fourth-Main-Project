from tkinter import *
from chat_response import *
LARGE_FONT= ("Verdana", 12)

class Pages(Tk):

    def __init__(self, *args, **kwargs):
        
        Tk.__init__(self, *args, **kwargs)
        Tk.title(self, "Fourth Year Main Assignment")

        container = Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self,parent)
        Tk.configure(self, bg="black")
        
        Label(self,text="Google AIY v/s Our Code", bg="blue", fg="white", font=("Helvetica", 16)).pack(fill=X)
        frame = Frame(self,width=250, bd=5, relief=SUNKEN, bg="red")
        frame.pack(side = LEFT, fill=Y, padx=5, pady=5)
        frame2 = Frame(self,width=250, bd=5, relief=SUNKEN, bg="red")
        frame2.pack(side = RIGHT, fill=Y, padx=5, pady=5)

        Label(frame, text="Google AIY", bg="black", fg="white", font=("Helvetica", 12)).pack(fill=X)
        Label(frame2, text="Our Code", bg="black", fg="white", font=("Helvetica", 12)).pack(fill=X)

        photo2 = PhotoImage(file="C:/Users/Ltrmex/Desktop/Fourth-Main-Project/Code/GUI/Images/GoogleAIY.png")
        Label(frame, image=photo2).pack()
        photo = PhotoImage(file="C:/Users/Ltrmex/Desktop/Fourth-Main-Project/Code/GUI/Images/Python.png")
        Label(frame2, image=photo).pack()

        button = Button(frame, text="Visit Google AIY", bg="blue", fg="white",
                            command=lambda: controller.show_frame(PageOne))
        button.pack(padx=20,pady=20)

        button2 = Button(frame2, text="Visit Our Code", bg="blue", fg="white",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack(padx=20,pady=20)


class PageOne(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        Tk.configure(self, bg="black")
        Label(self,text="Google AIY", bg="blue", fg="white", font=("Helvetica", 16)).pack(fill=X)

        photo2 = PhotoImage(file="C:/Users/Ltrmex/Desktop/Fourth-Main-Project/Code/GUI/Images/GoogleAIY.png")
        Label(self, image=photo2).pack()

        button1 = Button(self, text="Back to Main Menu", bg="red", fg="white",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack(padx=20,pady=20)

        button2 = Button(self, text="Our Code", bg="red", fg="white",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack(padx=20,pady=20)


class PageTwo(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        Tk.configure(self, bg="black")
        Label(self,text="Our Code", bg="blue", fg="white", font=("Helvetica", 16)).pack(fill=X)
		
        messages = Text(self)
        messages.pack()

        input_user = StringVar()
        input_field = Entry(self, text=input_user)
        input_field.pack(side=BOTTOM, fill=X)

        def Enter_pressed(event):
            input_get = input_field.get()
            print(input_get)
            messages.insert(INSERT, 'You: %s\nChatbot: %s\n' % input_get, userInput(input_get))
            # label = Label(self, text=input_get)
            input_user.set('')
            # label.pack()
            return "break"

        frame = Frame(self)  # , width=300, height=300)
        input_field.bind("<Return>", Enter_pressed)
        frame.pack()

        photo = PhotoImage(file="C:/Users/Ltrmex/Desktop/Fourth-Main-Project/Code/GUI/Images/Python.png")
        Label(self, image=photo).pack()

        button1 = Button(self, text="Back to Main Menu", bg="red", fg="white",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack(padx=20,pady=20)

        button2 = Button(self, text="Google AIY", bg="red", fg="white",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack(padx=20,pady=20)


app = Pages()
app.mainloop()