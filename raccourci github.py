import tkinter as tk
from tkinter import messagebox
import webbrowser

def open_website():
    messagebox.showinfo("Lancement de la page web", "Vous allez etre dirigé vers github")
    webbrowser.open("https://github.com/")

widget = tk.Tk()
widget.title("GitHub")

bouton = tk.Button(widget, text="Ouvrir GitHub", command=open_website)
bouton.pack(pady=10, padx=20)

widget.mainloop()
