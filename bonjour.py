import tkinter as tk
from tkinter import messagebox

def dire_bonjour():
    messagebox.showinfo("Message", "Bonjour")

fenetre = tk.Tk()
fenetre.title("Exemple de messagebox")

bouton = tk.Button(fenetre, text="Clique ici", command=dire_bonjour)
bouton.pack(pady=20, padx=20)

fenetre.mainloop()
