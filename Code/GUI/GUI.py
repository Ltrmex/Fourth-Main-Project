# Imports
from guizero import App, Text, TextBox, PushButton, Slider, Picture, Window

def openWindow():
    window.show(wait=True)

def closeWindow():
    window.hide()

app = App(title="Google AIY Voice Kit")

window = Window(app, title="2nd window")
window.hide()

panel1 = PushButton(app, text="Panel 1", grid=[0,0,0], command=openWindow)
panel2 = PushButton(app, text="Panel 2", grid=[1,0,0], command=openWindow)
panel3 = PushButton(app, text="Panel 3", grid=[2,0,0], command=openWindow)

closeButton = PushButton(window, text="Close", command=closeWindow)


app.display()