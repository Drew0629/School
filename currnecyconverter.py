from tkinter import * # Import whole module

class CurrencyConverter: # Create class
    def __init__(self): # Special method in Python class
        window = Tk() # Create application window
        window.title("Currency Converter") # Add title to application window
        window.configure(bg="yellow") #Add background color to application window

        # Adding Label widgets to application window
        Label(window,font="Helvetica 12 bold",bg="yellow",text ="Amount to Convert").grid(row=1, column=1,sticky =W)
        Label(window,font="Helvetica 12 bold",bg="yellow",text ="Conversion Rate").grid(row=2, column=1,sticky =W)
        Label(window,font="Helvetica 12 bold",bg="yellow",text ="Converted Amount").grid(row=3, column=1,sticky =W)

        # Create objects and add entry functions
        self.amounttoConvertVar = StringVar()
        Entry(window, textvariable = self.amounttoConvertVar, justify = RIGHT).grid(row=1,column=2)
        self.conversionRateVar = StringVar()
        Entry(window, textvariable = self.conversionRateVar, justify = RIGHT).grid(row=2,column=2)
        self.convertedAmountVar = StringVar()
        lblConvertedAmount =Label(window,font="Helvetica 12 bold", bg="yellow", textvariable = self.convertedAmountVar).grid(row=3,column=2,sticky = E)

        # Create convert and clear buttons . When clicked they will call their respective functions.
        btConvertedAmount = Button(window, text = "Convert",font="Helvetica 12 bold",bg="blue",fg="white",command = self.ConvertedAmount).grid(row = 4,column=2,sticky = E)
        btdelete_all = Button(window, text = "Clear",font="Helvetica 12 bold",bg="red",fg="white",command = self.delete_all).grid(row = 4,column=6,padx=25,pady=25,sticky = E)

        window.mainloop() # Runs the application program

        # Function to do the converison. Stores inputs and performs conversion 
