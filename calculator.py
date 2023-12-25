import tkinter as tk

class Calculator():
    def __init__(self, tk_Frame: tk.Frame):
        self.tk_Frame = tk_Frame

        # Entry Variables
        self.User_Input = None
        self.input_box_width = 30
        self.User_Input_txt = ""

        # Creating the calculator
        self.Input()
        self.Buttons()
        
    def Input(self):
        self.User_Input_txt = tk.StringVar()
        self.User_Input = tk.Entry(self.tk_Frame, width=self.input_box_width,
                                   textvariable=self.User_Input_txt)
        self.User_Input.grid(row=0, column=0, 
                             columnspan=3, padx=5, pady=5)
        return self.User_Input.get()
    
    def Buttons(self):
        button0 = tk.Button(self.tk_Frame, text="0", width=10, command = lambda: self.ButtonAdd("0")).grid(row=1, column=0)
        button1 = tk.Button(self.tk_Frame, text="1", width=10, command = lambda: self.ButtonAdd("1")).grid(row=1, column=1)
        button2 = tk.Button(self.tk_Frame, text="2", width=10, command = lambda: self.ButtonAdd("2")).grid(row=1, column=2)
        button3 = tk.Button(self.tk_Frame, text="3", width=10, command = lambda: self.ButtonAdd("3")).grid(row=2, column=0)
        button4 = tk.Button(self.tk_Frame, text="4", width=10, command = lambda: self.ButtonAdd("4")).grid(row=2, column=1)
        button5 = tk.Button(self.tk_Frame, text="5", width=10, command = lambda: self.ButtonAdd("5")).grid(row=2, column=2)
        button6 = tk.Button(self.tk_Frame, text="6", width=10, command = lambda: self.ButtonAdd("6")).grid(row=3, column=0)
        button7 = tk.Button(self.tk_Frame, text="7", width=10, command = lambda: self.ButtonAdd("7")).grid(row=3, column=1)
        button8 = tk.Button(self.tk_Frame, text="8", width=10, command = lambda: self.ButtonAdd("8")).grid(row=3, column=2)
        button9 = tk.Button(self.tk_Frame, text="9", width=10, command = lambda: self.ButtonAdd("9")).grid(row=4, column=0)
        button_sum = tk.Button(self.tk_Frame, text="+", width=10, command = lambda: self.ButtonAdd("+")).grid(row=4, column=1)
        button_sub = tk.Button(self.tk_Frame, text="-", width=10, command = lambda: self.ButtonAdd("-")).grid(row=4, column=2)
        button_prod = tk.Button(self.tk_Frame, text="*", width=10, command = lambda: self.ButtonAdd("*")).grid(row=5, column=0)
        button_div = tk.Button(self.tk_Frame, text="/", width=10, command = lambda: self.ButtonAdd("/")).grid(row=5, column=1)
        button_equal = tk.Button(self.tk_Frame, text="=", width=10, command = self.calculate).grid(row=5, column=2)
        button_back = tk.Button(self.tk_Frame, text="Back", width=10, command = self.backspace).grid(row=6, column=0)
        button_clear = tk.Button(self.tk_Frame, text="clear", width=10, command = self.clearScreen).grid(row=6, column=1)
    
    def ButtonAdd(self, button_value: str):
        self.User_Input_txt.set(self.User_Input.get() + button_value)

    def calculate(self):
        self.User_Input_txt.set(eval(self.User_Input.get()))
    
    def backspace(self):
        self.User_Input_txt.set(self.User_Input.get()[0:(len(self.User_Input.get()) - 1)])

    def clearScreen(self):
        self.User_Input_txt.set("")
        
# Calling the class calculator
root = tk.Tk()
root.title("Py Calculator")
myCalculator = Calculator(root)
root.mainloop()