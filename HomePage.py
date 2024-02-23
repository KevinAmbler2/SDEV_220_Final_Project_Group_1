import tkinter as tk
from tkinter import ttk

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_label = tk.Label(self, image=controller.images["HomePage"])
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Button to go to MenuCartPage
        menu_button = ttk.Button(self, text="Go to Menu", command=lambda: controller.show_frame("MenuCartPage"))
        menu_button.pack()
        # Forced Exit from the application
        exit_button = ttk.Button(self, text="Exit", command=self.controller.quit)
        exit_button.pack()