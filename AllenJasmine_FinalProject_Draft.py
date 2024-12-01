"""

Author:  Jasmine Allen
Date written: 11/15/24 - 11/26/24
Assignment:   Final Project Draft
Short Desc:   My final project first draft, it currently contains code to have two working drop down menus for selecting phone model and phone case color.


"""

import tkinter as tk

root = tk.Tk()
root.title("Phone Case Customizer")

frame = tk.Frame(root)
frame.grid(row=0, column=0, sticky="nsew")

frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

class Main:
    #Function for choosing phone type
    def phoneMenu(self):
        typesLabel = tk.Label(frame, text="Phone Model:")
        typesLabel.grid(row=0, column=0, sticky="w")

        phoneTypes = ["iPhone", "Android", "Google Pixel"]

        selectedPhone = tk.StringVar(frame)
        selectedPhone.set("Select your phone model")

        selectMenu = tk.OptionMenu(frame, selectedPhone, *phoneTypes)
        selectMenu.grid(row=1, column=0, sticky="ew")

        def print_answers():
            print(selectedPhone.get())
            return None

        submit_button = tk.Button(frame, text="Submit", command=print_answers)
        submit_button.grid(row=1, column=1)

    #Function for choosing case color
    def caseColor(self):
        colorLabel = tk.Label(frame, text="Case Color:")
        colorLabel.grid(row=2, column=0, sticky="w")

        caseColors = ["Red", "Blue", "Yellow"]

        selectedColor = tk.StringVar(frame)
        selectedColor.set("Select the case color")
    
        selectMenu = tk.OptionMenu(frame, selectedColor, *caseColors)
        selectMenu.grid(row=3, column=0, sticky="ew")
    
        def print_answer():
            global globalColor
            if selectedColor.get() == "Blue":
                print("Correct!")
                globalColor = "Blue"
                print(globalColor)
            elif selectedColor.get() == "Red":
                print("Correct!")
                globalColor = "Red"
                print(globalColor)
            elif selectedColor.get() == "Yellow":
                print("Correct!")
                globalColor = "Yellow"
                print(globalColor)
            else: 
                print("Nah")
            return None

        submit_button = tk.Button(frame, text="Submit", command=print_answer)
        submit_button.grid(row=3, column=1)

def globalVariables():
    global globalColor
    globalColor = None
    global globalModel
    globalModel = None

def printCheck():
    print(globalColor)

submit_button = tk.Button(frame, text="Preview", command=printCheck)
submit_button.grid(row=4, column=1)

globalVariables()

#Execute Functions
fullApp = Main()
fullApp.phoneMenu()
fullApp.caseColor()
root.mainloop()