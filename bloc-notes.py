import tkinter as tk
from tkinter import filedialog, messagebox

class BlocNotes(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Bloc-Notes")
        self.geometry("600x400")

        self.text_area = tk.Text(self, wrap="word")
        self.text_area.pack(fill="both", expand=True)

        self.create_menu()

    def create_menu(self):
        menu_bar = tk.Menu(self)
        self.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Nouveau", command=self.nouveau_fichier)
        file_menu.add_command(label="Ouvrir", command=self.ouvrir_fichier)
        file_menu.add_command(label="Enregistrer", command=self.enregistrer_fichier)
        file_menu.add_separator()
        file_menu.add_command(label="Quitter", command=self.quit)

        menu_bar.add_cascade(label="Fichier", menu=file_menu)

    def nouveau_fichier(self):
        self.text_area.delete(1.0, tk.END)

    def ouvrir_fichier(self):
        fichier = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Fichiers texte", "*.txt"), ("Tous les fichiers", "*.*")])
        if fichier:
            with open(fichier, "r", encoding="utf-8") as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, file.read())

    def enregistrer_fichier(self):
        fichier = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Fichiers texte", "*.txt"), ("Tous les fichiers", "*.*")])
        if fichier:
            with open(fichier, "w", encoding="utf-8") as file:
                file.write(self.text_area.get(1.0, tk.END))

if __name__ == "__main__":
    app = BlocNotes()
    app.mainloop()
