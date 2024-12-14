"""

Author:  Jasmine Allen
Date written: 11/15/24 - 12/14/24
Assignment:   Final Project
Short Desc:   This is a program that has a GUI that allows the user to create a custom phone case by allowing the user to select their desired phone model and then also select two different colors for the case. There is a button to preview the end result which causes a window to open and show a preview of the finished case. Another button labeled "Finish" will calculate the price of the case based off the currently selected colors. The final button is labeled "Close" and simply closes the program.

"""

import customtkinter

from PIL import Image

# Sets up some global variables
def globalVariable():
    global finalPreview # Makes the finalPreview variable global
    finalPreview = None # Variable that will be used to tell the program which image to display as the preview.

globalVariable() # Activates the globalVariable function

# Changes the color of the GUI to match the user's system theme
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

# Initializes the secondary preview window of the program
class previewWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("300x500")
        self.title("Preview")

        # Creates and places an empty label that will hold the preview image
        self.imageLabel = customtkinter.CTkLabel(self, text="", image=finalPreview) # Label used to display the preview image in the secondary window
        self.imageLabel.grid(row = 0, column = 0, padx = 0, pady = 0)

# Initializes the main window of the program
class PhoneCustomizer(customtkinter.CTk):
    # Contains all the GUI widgets and sets up the variables needed to make each widget work.
    def __init__(self, *args, **kwargs):
        self.primary = None # Keeps track of the primary color that has been selected
        self.secondary = None # Keeps track of the secondary color that has been selected
        self.phoneModel = None # Keeps track of the phone model that has been selected
        self.finalPrice = "0.00" # Keeps track of the final price of the case based off the selected colors
        super().__init__(*args, **kwargs)
        self.geometry("370x300")
        self.title("Phone Case Customizer")

        # Detects the varios phone model selections
        def phoneModelSelection(choice):
            if choice == "iPhone":
                self.phoneModel = "iPhone"
                self.endResult()
            elif choice == "Samsung Galaxy":
                self.phoneModel = "Samsung Galaxy"
                self.endResult()
            elif choice == "Google Pixel":
                self.phoneModel = "Google Pixel"
                self.endResult()

        # Sets up and displays the menu for selecting phone model as well as creating a label that tells the user what the menu does
        self.phoneLabel = customtkinter.CTkLabel(self, text="Select phone model here:") # Label that instructs the user to pick a phone model
        self.phoneLabel.grid(row = 0, column = 0, padx = 20, pady = 2, sticky = "NW")
        self.phoneModels = customtkinter.CTkComboBox(self, 
                                                  values=["iPhone", "Samsung Galaxy", "Google Pixel"], 
                                                  command=phoneModelSelection) # Creates a drop down menu that allows the user to select their desired phone model
        self.phoneModels.set("Select model")
        self.phoneModels.grid(row = 1, column = 0, padx = 0, pady = 10)

        # Images that display the chosen colors
        self.redColor = customtkinter.CTkImage(light_image=Image.open("previewimages/red.png"), size=(150,25)) # Displays the color red
        self.blueColor = customtkinter.CTkImage(light_image=Image.open("previewimages/blue.png"), size=(150,25)) # Displays the color blue
        self.yellowColor = customtkinter.CTkImage(light_image=Image.open("previewimages/yellow.png"), size=(150,25)) # Displays the color yellow

        # Detects the different primary case color selections
        def primaryColorSelection(choice):
            if choice == "Red":
                self.primaryColorLabel.configure(image=self.redColor)
                self.primary = "Red" # Changes the self.primary variable to equal "Red"
                self.endResult() # Activates the endResult method
            elif choice == "Blue":
                self.primaryColorLabel.configure(image=self.blueColor)
                self.primary = "Blue" # Changes the self.primary variable to equal "Blue"
                self.endResult() # Activates the endResult method
            elif choice == "Yellow":
                self.primaryColorLabel.configure(image=self.yellowColor)
                self.primary = "Yellow" # Changes the self.primary variable to equal "Yellow"
                self.endResult() # Activates the endResult method

        # Sets up and displays the menu for selecting primary phone case color
        self.colorsLabel = customtkinter.CTkLabel(self, text="Select colors here:") # Label that instructs the user to pick the colors they want for their case
        self.colorsLabel.grid(row = 2, column = 0, padx = 20, pady = 0, sticky = "NW")
        self.primaryColor = customtkinter.CTkComboBox(self, 
                                                  values=["Red", "Blue", "Yellow"], 
                                                  command=primaryColorSelection) # Creates a drop down menu that allows the user to select their desired main color for their case
        self.primaryColor.set("Select color")
        self.primaryColor.grid(row = 3, column = 0, padx = 20, pady = 10)
        self.primaryColorLabel = customtkinter.CTkLabel(self, text="", image=None) # Label that is used to display the currently selected color
        self.primaryColorLabel.grid(row = 3, column = 1, padx = 20, pady = 10)

        # Detects the different secondary case color selections
        def secondaryColorSelection(choice):
            if choice == "Red":
                self.secondaryColorLabel.configure(image=self.redColor)
                self.secondary = "Red" # Changes the self.secondary variable to equal "Red"
                self.endResult() # Activates the endResult method
            elif choice == "Blue":
                self.secondaryColorLabel.configure(image=self.blueColor)
                self.secondary = "Blue" # Changes the self.secondary variable to equal "Blue"
                self.endResult() # Activates the endResult method
            elif choice == "Yellow":
                self.secondaryColorLabel.configure(image=self.yellowColor)
                self.secondary = "Yellow" # Changes the self.secondary variable to equal "Yellow"
                self.endResult() # Activates the endResult method

        # Sets up and displays the menu for selecting secondary phone case color
        self.secondaryColor = customtkinter.CTkComboBox(self, 
                                                  values=["Red", "Blue", "Yellow"], 
                                                  command=secondaryColorSelection) # Creates a drop down menu that allows the user to select their desired second color for their case
        self.secondaryColor.set("Select color")
        self.secondaryColor.grid(row = 4, column = 0, padx = 20, pady = 2)
        self.secondaryColorLabel = customtkinter.CTkLabel(self, text="", image=None) # Label that is used to display the currently selected color
        self.secondaryColorLabel.grid(row = 4, column = 1, padx = 20, pady = 0)

        # Sets up the preview button that opens the preview window
        self.previewButton = customtkinter.CTkButton(self, text="Preview", command=self.openPreview) # Button to open the preview window and let the user see a preview of their phone case
        self.previewButton.grid(row = 6, column = 1, padx = 20, pady = 5)
        self.previewWindow = None # Variable used to determine whether or not the preview window is open

        # Sets up the cost calculation button
        self.finishButton = customtkinter.CTkButton(self, text="Finish", command=self.costCalc) # Button to calculate the price of the currently selected colors
        self.finishButton.grid(row = 6, column = 0, padx = 20, pady = 5)
        self.finishLabel = customtkinter.CTkLabel(self, text=f"Final price is: ${self.finalPrice}") # Label that displays the price calculated after pressing the Finish button
        self.finishLabel.grid(row = 5, column = 0, padx = 20, pady = 0, columnspan = 2)

        # Sets up the close button
        self.closeButton = customtkinter.CTkButton(self, text="Close", command=self.closeProgram) # Button that gives the user an in-GUI way to close the program
        self.closeButton.grid(row = 7, column = 0, padx = 20, pady = 5, columnspan = 2)

    # Method for closing the program
    def closeProgram(self):
        exit()
        
    # Method that detects which color combination is currently selected and chooses the corresponding preview image to display. This particular method only runs if the user has selected iPhone as their phone model
    def iphoneResult(self):
            global finalPreview
            if self.primary == "Red" and self.secondary == "Red": # Checks to see if the user selected red as both colors
                iphoneOne = customtkinter.CTkImage(light_image=Image.open("previewimages/iphone/iphoneRed.png"), size=(300,500)) # Image of a purely red iPhone phone case
                finalPreview = iphoneOne # Changes the finalPreview variable to be equal to the iphoneOne variable
            elif self.primary == "Red" and self.secondary == "Blue":
                iphoneTwo = customtkinter.CTkImage(light_image=Image.open("previewimages/iphone/iphoneRedandBlue.png"), size=(300,500)) # Image of a red and blue iPhone phone case
                finalPreview = iphoneTwo # Changes the finalPreview variable to be equal to the iphoneTwo variable
            elif self.primary == "Red" and self.secondary == "Yellow":
                iphoneThree = customtkinter.CTkImage(light_image=Image.open("previewimages/iphone/iphoneRedandYellow.png"), size=(300,500)) # Image of a red and yellow iPhone phone case
                finalPreview = iphoneThree # Changes the finalPreview variable to be equal to the iphoneThree variable
            elif self.primary == "Blue" and self.secondary == "Red":
                iphoneFour = customtkinter.CTkImage(light_image=Image.open("previewimages/iphone/iphoneBlueandRed.png"), size=(300,500)) # Image of a blue and red iPhone phone case
                finalPreview = iphoneFour # Changes the finalPreview variable to be equal to the iphoneFour variable
            elif self.primary == "Blue" and self.secondary == "Blue":
                iphoneFive = customtkinter.CTkImage(light_image=Image.open("previewimages/iphone/iphoneBlue.png"), size=(300,500)) # Image of a purely blue iPhone phone case
                finalPreview = iphoneFive # Changes the finalPreview variable to be equal to the iphoneFive variable
            elif self.primary == "Blue" and self.secondary == "Yellow":
                iphoneSix = customtkinter.CTkImage(light_image=Image.open("previewimages/iphone/iphoneBlueandYellow.png"), size=(300,500)) # Image of a blue and yellow iPhone phone case
                finalPreview = iphoneSix # Changes the finalPreview variable to be equal to the iphoneSix variable
            elif self.primary == "Yellow" and self.secondary == "Red":
                iphoneSeven = customtkinter.CTkImage(light_image=Image.open("previewimages/iphone/iphoneYellowandRed.png"), size=(300,500)) # Image of a yellow and red iPhone phone case
                finalPreview = iphoneSeven # Changes the finalPreview variable to be equal to the iphoneSeven variable
            elif self.primary == "Yellow" and self.secondary == "Blue":
                iphoneEight = customtkinter.CTkImage(light_image=Image.open("previewimages/iphone/iphoneYellowandBlue.png"), size=(300,500)) # Image of a yellow and blue iPhone phone case
                finalPreview = iphoneEight # Changes the finalPreview variable to be equal to the iphoneEight variable
            elif self.primary == "Yellow" and self.secondary == "Yellow":
                iphoneNine = customtkinter.CTkImage(light_image=Image.open("previewimages/iphone/iphoneYellow.png"), size=(300,500)) # Image of a purely yellow iPhone phone case
                finalPreview = iphoneNine # Changes the finalPreview variable to be equal to the iphoneNine variable

    # Method that detects which color combination is currently selected and chooses the corresponding preview image to display. This particular method only runs if the user has selected Samsung Galaxy as their phone model
    def galaxyResult(self):
            global finalPreview
            if self.primary == "Red" and self.secondary == "Red":
                galaxyOne = customtkinter.CTkImage(light_image=Image.open("previewimages/galaxy/galaxyRed.png"), size=(300,500)) # Image of a purely red Samsung Galaxy phone case
                finalPreview = galaxyOne # Changes the finalPreview variable to be equal to the galaxyOne variable
            elif self.primary == "Red" and self.secondary == "Blue":
                galaxyTwo = customtkinter.CTkImage(light_image=Image.open("previewimages/galaxy/galaxyRedandBlue.png"), size=(300,500)) # Image of a red and blue Samsung Galaxy phone case
                finalPreview = galaxyTwo # Changes the finalPreview variable to be equal to the galaxyTwo variable
            elif self.primary == "Red" and self.secondary == "Yellow":
                galaxyThree = customtkinter.CTkImage(light_image=Image.open("previewimages/galaxy/galaxyRedandYellow.png"), size=(300,500)) # Image of a red and yellow Samsung Galaxy phone case
                finalPreview = galaxyThree # Changes the finalPreview variable to be equal to the galaxyThree variable
            elif self.primary == "Blue" and self.secondary == "Red":
                galaxyFour = customtkinter.CTkImage(light_image=Image.open("previewimages/galaxy/galaxyBlueandRed.png"), size=(300,500)) # Image of a blue and red Samsung Galaxy phone case
                finalPreview = galaxyFour # Changes the finalPreview variable to be equal to the galaxyFour variable
            elif self.primary == "Blue" and self.secondary == "Blue":
                galaxyFive = customtkinter.CTkImage(light_image=Image.open("previewimages/galaxy/galaxyBlue.png"), size=(300,500)) # Image of a purely blue Samsung Galaxy phone case
                finalPreview = galaxyFive # Changes the finalPreview variable to be equal to the galaxyFive variable
            elif self.primary == "Blue" and self.secondary == "Yellow":
                galaxySix = customtkinter.CTkImage(light_image=Image.open("previewimages/galaxy/galaxyBlueandYellow.png"), size=(300,500)) # Image of a blue and yellow Samsung Galaxy phone case
                finalPreview = galaxySix # Changes the finalPreview variable to be equal to the galaxySix variable
            elif self.primary == "Yellow" and self.secondary == "Red":
                galaxySeven = customtkinter.CTkImage(light_image=Image.open("previewimages/galaxy/galaxyYellowandRed.png"), size=(300,500)) # Image of a yellow and red Samsung Galaxy phone case
                finalPreview = galaxySeven # Changes the finalPreview variable to be equal to the galaxySeven variable
            elif self.primary == "Yellow" and self.secondary == "Blue":
                galaxyEight = customtkinter.CTkImage(light_image=Image.open("previewimages/galaxy/galaxyYellowandBlue.png"), size=(300,500)) # Image of a yellow and blue Samsung Galaxy phone case
                finalPreview = galaxyEight # Changes the finalPreview variable to be equal to the galaxyEight variable
            elif self.primary == "Yellow" and self.secondary == "Yellow":
                galaxyNine = customtkinter.CTkImage(light_image=Image.open("previewimages/galaxy/galaxyYellow.png"), size=(300,500)) # Image of a purely yellow Samsung Galaxy phone case
                finalPreview = galaxyNine # Changes the finalPreview variable to be equal to the galaxyNine variable

    # Method that detects which color combination is currently selected and chooses the corresponding preview image to display. This particular method only runs if the user has selected Google Pixel as their phone model
    def pixelResult(self):
            global finalPreview
            if self.primary == "Red" and self.secondary == "Red":
                pixelOne = customtkinter.CTkImage(light_image=Image.open("previewimages/pixel/pixelRed.png"), size=(300,500)) # Image of a purely red Google Pixel phone case
                finalPreview = pixelOne # Changes the finalPreview variable to be equal to the pixelOne variable
            elif self.primary == "Red" and self.secondary == "Blue":
                pixelTwo = customtkinter.CTkImage(light_image=Image.open("previewimages/pixel/pixelRedandBlue.png"), size=(300,500)) # Image of a red and blue Google Pixel phone case
                finalPreview = pixelTwo # Changes the finalPreview variable to be equal to the pixelTwo variable
            elif self.primary == "Red" and self.secondary == "Yellow":
                pixelThree = customtkinter.CTkImage(light_image=Image.open("previewimages/pixel/pixelRedandYellow.png"), size=(300,500)) # Image of a red and yellow Google Pixel phone case
                finalPreview = pixelThree # Changes the finalPreview variable to be equal to the pixeThree variable
            elif self.primary == "Blue" and self.secondary == "Red":
                pixelFour = customtkinter.CTkImage(light_image=Image.open("previewimages/pixel/pixelBlueandRed.png"), size=(300,500)) # Image of a blue and red Google Pixel phone case
                finalPreview = pixelFour # Changes the finalPreview variable to be equal to the pixelFour variable
            elif self.primary == "Blue" and self.secondary == "Blue":
                pixelFive = customtkinter.CTkImage(light_image=Image.open("previewimages/pixel/pixelBlue.png"), size=(300,500)) # Image of a purely blue Google Pixel phone case
                finalPreview = pixelFive # Changes the finalPreview variable to be equal to the pixelFive variable
            elif self.primary == "Blue" and self.secondary == "Yellow":
                pixelSix = customtkinter.CTkImage(light_image=Image.open("previewimages/pixel/pixelBlueandYellow.png"), size=(300,500)) # Image of a blue and yellow Google Pixel phone case
                finalPreview = pixelSix # Changes the finalPreview variable to be equal to the pixelSix variable
            elif self.primary == "Yellow" and self.secondary == "Red":
                pixelSeven = customtkinter.CTkImage(light_image=Image.open("previewimages/pixel/pixelYellowandRed.png"), size=(300,500)) # Image of a yellow and red Google Pixel phone case
                finalPreview = pixelSeven # Changes the finalPreview variable to be equal to the pixelSeven variable
            elif self.primary == "Yellow" and self.secondary == "Blue":
                pixelEight = customtkinter.CTkImage(light_image=Image.open("previewimages/pixel/pixelYellowandBlue.png"), size=(300,500)) # Image of a yellow and blue Google Pixel phone case
                finalPreview = pixelEight # Changes the finalPreview variable to be equal to the pixelEight variable
            elif self.primary == "Yellow" and self.secondary == "Yellow":
                pixelNine = customtkinter.CTkImage(light_image=Image.open("previewimages/pixel/pixelYellow.png"), size=(300,500)) # Image of a purely yellow Google Pixel phone case
                finalPreview = pixelNine # Changes the finalPreview variable to be equal to the pixelNine variable

    # Method that detects which type of phone model the user has selected and runs the corresponding method to check for color
    def endResult(self):
        if self.phoneModel == "iPhone":
            self.iphoneResult() # Runs the self.iphoneResult method to determine which preview image to display
        elif self.phoneModel == "Samsung Galaxy":
            self.galaxyResult() # Runs the self.galaxyResult method to determine which preview image to display
        elif self.phoneModel == "Google Pixel":
            self.pixelResult() # Runs the self.pixelResult method to determine which preview image to display
        else:
            pass # If no phone model has been chosen then don't display anything
        
    # Method that detects if the preview window is already open and, if it isn't, opens it
    def openPreview(self):
        if self.previewWindow is None or not self.previewWindow.winfo_exists():
            self.previewWindow = previewWindow(self) # If the preview window is not already open, then this method opens it
        else:
            self.previewWindow.focus() # If the preview window is already open then instead of opening it again this method causes the preview window to be pulled to the front

    # Checks to see how many different colors are actually being used in the case and then sets the price based on number of unique colors
    def costCalc(self):
        if self.primary == None and self.secondary == None:
            pass # If not colors are selected then keep the self.finalPrice value as the default 0.00
        elif self.primary == self.secondary:
            self.finalPrice = "20.00" # If the self.primary and self.secondary colors are set to the same color then set the price to $20
            self.finishLabel.configure(text = f"Final price is: ${self.finalPrice}")
        elif self.primary != self.secondary:
            self.finalPrice = "40.00" # If the self.primary and self.secondary colors are set to different colors then set the price to $40
            self.finishLabel.configure(text = f"Final price is: ${self.finalPrice}")

# Activates the program
if __name__ == "__main__":
    app = PhoneCustomizer() # Makes the PhoneCustomizer class equal to the app variable
    app.mainloop() # Starts the loop