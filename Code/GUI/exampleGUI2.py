# Imports
from guizero import App, Combo, Text, CheckBox 

# Set app name
app = App(title="My second GUI app", width=300, height=200, layout="grid")

# Dropdown menu widget
filmDescription = Text(app, text="Which film?", grid=[0,0], align="left")   # text widget for Dropdown
filmChoice = Combo(app, options=["Star Wars", "Frozen", "Lion King"], grid=[1,0], align="left") # dropdown

# Checkbox widget
filmDescription = Text(app, text="Seat type: ", grid=[0,0], align="left")   # text widget for checkbox
vipSeat = CheckBox(app, text="VIP seat?", grid=[1,1], align="left") # checkbox

# Display app window
app.display()