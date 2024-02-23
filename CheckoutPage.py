import tkinter as tk
from tkinter import ttk

class CheckoutPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_label = tk.Label(self, image=controller.images["CheckoutPage"])
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Button to go back to HomePage
        home_button = ttk.Button(self, text="Return Home", command=lambda: controller.show_frame("HomePage"))
        home_button.pack()
        # Forced Exit from the application
        exit_button = ttk.Button(self, text="Exit", command=self.controller.quit)
        exit_button.pack()