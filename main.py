'''
Hunter - Homepage window + Window superclass
Kevin - Menu and Cart windows + Menu and Cart classes
Mang - Checkout window + Order class
Argyrios - Initial creation of window objects and managing styling

'''
import tkinter as tk
from tkinter import ttk
from Images import *
from HomePage import *
from MenuCartPage import *
from CheckoutPage import *


class PizzaApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Luigi's Pizzeria")
        self.geometry("800x600")

        # Loading images directly with Tkinter
        self.images = {name: tk.PhotoImage(file=path) for name, path in image_paths.items()}
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (HomePage, MenuCartPage, CheckoutPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


if __name__ == "__main__":
    app = PizzaApp()
    app.mainloop()