import tkinter as tk
from tkinter import messagebox
import string
import secrets
import pyperclip  # Pour copier automatiquement le mot de passe

def generer_mot_de_passe():
    try:
        longueur = int(entree_longueur.get())
        if longueur < 4:
            messagebox.showwarning("Erreur", "La longueur doit être d'au moins 4 caractères.")
            return
        caracteres = string.ascii_letters + string.digits + string.punctuation
        mot_de_passe = ''.join(secrets.choice(caracteres) for _ in range(longueur))
        champ_resultat.config(state='normal')
        champ_resultat.delete(0, tk.END)
        champ_resultat.insert(0, mot_de_passe)
        champ_resultat.config(state='readonly')
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer un nombre valide.")

def copier():
    mot_de_passe = champ_resultat.get()
    if mot_de_passe:
        pyperclip.copy(mot_de_passe)
        messagebox.showinfo("Copié", "Mot de passe copié dans le presse-papiers !")

# Création de l'interface
fenetre = tk.Tk()
fenetre.title("Générateur de Mot de Passe")
fenetre.geometry("400x200")
fenetre.config(bg="#2b2b2b")

label_titre = tk.Label(fenetre, text="Générateur de mot de passe", fg="white", bg="#2b2b2b", font=("Arial", 14, "bold"))
label_titre.pack(pady=10)

frame = tk.Frame(fenetre, bg="#2b2b2b")
frame.pack()

label_longueur = tk.Label(frame, text="Longueur :", fg="white", bg="#2b2b2b")
label_longueur.grid(row=0, column=0, padx=5)

entree_longueur = tk.Entry(frame, width=5)
entree_longueur.grid(row=0, column=1)

bouton_generer = tk.Button(frame, text="Générer", command=generer_mot_de_passe)
bouton_generer.grid(row=0, column=2, padx=10)

champ_resultat = tk.Entry(fenetre, font=("Arial", 12), justify="center", state="readonly", width=30)
champ_resultat.pack(pady=10)

bouton_copier = tk.Button(fenetre, text="Copier", command=copier)
bouton_copier.pack()

fenetre.mainloop()
