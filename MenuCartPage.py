import tkinter as tk
from tkinter import ttk

class MenuCartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_label = tk.Label(self, image=controller.images["MenuCartPage"])
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Button to go to CheckoutPage
        checkout_button = ttk.Button(self, text="Proceed to Checkout", command=lambda: controller.show_frame("CheckoutPage"))
        checkout_button.pack()
        # Forced Exit from the application
        exit_button = ttk.Button(self, text="Exit", command=self.controller.quit)
        exit_button.pack()