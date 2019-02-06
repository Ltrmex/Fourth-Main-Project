# Imports
from guizero import App, Text

# Set app name
app = App(title="Hello world")

# Widgets (text, text boxes, buttons, etc)
welcomeMessage = Text(app, text="Welcome to my app", size=40, font="Times New Roman", color="lightblue")

# Display app window
app.display()   