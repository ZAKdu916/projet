import tkinter as tk
from tkinter import messagebox

def premier_message():
    messagebox.showinfo("rappel", "prendre ses medicaments")

def deuxieme_message():
    messagebox.showinfo("rappel", "boire de l'eau")

def trois_message():
    messagebox.showinfo("rappel", "aller travailler")

def dernier_rappel():
    messagebox.showinfo("rappel", "aller dormir")

fenetre = tk.Tk()
fenetre.title("rappels quotidiens")

bouton1 = tk.Button(fenetre, text="Clique ici", command=premier_message)
bouton1.pack(pady=10, padx=20)

bouton2 = tk.Button(fenetre, text="Clique ici", command=deuxieme_message)
bouton2.pack(pady=10, padx=20)

bouton3 = tk.Button(fenetre, text="Clique ici", command=trois_message)
bouton3.pack(pady=10, padx=20)

bouton2 = tk.Button(fenetre, text="Clique ici", command=dernier_rappel)
bouton2.pack(pady=10, padx=20)

fenetre.mainloop()


