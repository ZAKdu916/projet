import tkinter as tk
import sqlite3


conn = sqlite3.connect('taches.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS taches (
                    id INTEGER PRIMARY KEY,
                    tache TEXT NOT NULL)''')
conn.commit()


def ajouter_tache():
    tache = entry.get()
    if tache:
        cursor.execute('INSERT INTO taches (tache) VALUES (?)', (tache,))
        conn.commit()
        entry.delete(0, tk.END)
        afficher_taches()


def afficher_taches():
    listbox.delete(0, tk.END)
    cursor.execute('SELECT * FROM taches')
    for row in cursor.fetchall():
        listbox.insert(tk.END, row[1])


def supprimer_tache():
    selection = listbox.curselection()
    if selection:
        tache = listbox.get(selection[0])
        cursor.execute('DELETE FROM taches WHERE tache = ?', (tache,))
        conn.commit()
        afficher_taches()


root = tk.Tk()
root.title("Gestionnaire de Tâches")
root.geometry("400x400")

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

ajouter_btn = tk.Button(root, text="Ajouter", font=("Arial", 14), command=ajouter_tache)
ajouter_btn.pack()

listbox = tk.Listbox(root, font=("Arial", 14))
listbox.pack(pady=10, fill=tk.BOTH, expand=True)

supprimer_btn = tk.Button(root, text="Supprimer", font=("Arial", 14), command=supprimer_tache)
supprimer_btn.pack()


afficher_taches()

root.mainloop()


conn.close()
