import tkinter as tk
from tkinter import messagebox
import webbrowser

def raccourci():
    messagebox.showinfo("Cliquez sur OK pour acceder au site", "Google s'ouvrira sur votre navigateur par default")
    webbrowser.open("https://www.google.com/")

fenetre = tk.Tk()
fenetre.title("Raccourci Google")

bouton = tk.Button(fenetre, text="Cliquez ici", command=raccourci)
bouton.pack(pady=10, padx=20)

fenetre.mainloop()
