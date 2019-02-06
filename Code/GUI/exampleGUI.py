# Imports
from guizero import App, Text, TextBox, PushButton 

# Method responsible for changing the value of welcomeMessage
def displayMyName():
    welcomeMessage.value = myName.value
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

# Display app window
app.display()   