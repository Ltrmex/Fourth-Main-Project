# Imports
from guizero import App, Text, TextBox, PushButton, Slider, Picture 

# Method responsible for changing the value of welcomeMessage
def displayMyName():
    welcomeMessage.value = myName.value
    return

# Method responsible for changing text size value
def changeTextSize(sliderValue):
    welcomeMessage.size = sliderValue
    return

# Set app name
app = App(title="Hello world")

# Widgets (text, text boxes, buttons, etc)
# Text widget
welcomeMessage = Text(app, text="Welcome to my app", size=40, font="Times New Roman", color="lightblue")

# Text box widget
myName = TextBox(app)

# Update text button
updateText = PushButton(app, command=displayMyName, text="Display my name")

# Slider widget
textSize = Slider(app, command=changeTextSize, start=10, end=80)

# Picture widget
image = Picture(app, image="C:/Users/Ltrmex/Desktop/Fourth-Main-Project/Code/GUI/Images/Python.png")

# Display app window
app.display()   