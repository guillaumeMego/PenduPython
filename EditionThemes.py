from PenduDb import PenduDb
from tkinter import *
from tkinter import simpledialog, messagebox

class EditionThemes:
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.fenetre.title("Edition des thèmes")
        self.fenetre.resizable(False, False)
        self.fenetre.protocol("WM_DELETE_WINDOW", self.fermer_fenetre)
        self.fenetre.geometry("400x400")

        self.db = PenduDb()  # Instanciation de la classe PenduDb

        self.frame = Frame(self.fenetre)
        self.frame.pack(padx=10, pady=10)

        self.label = Label(self.frame, text="Liste des thèmes")
        self.label.pack(padx=10, pady=10)

        self.listbox = Listbox(self.frame)
        self.listbox.pack(padx=10, pady=10)

        self.bouton_ajouter = Button(self.frame, text="Ajouter un thème", command=self.ajouter_theme)
        self.bouton_ajouter.pack(padx=10, pady=5)

        self.bouton_modifier = Button(self.frame, text="Modifier le thème", command=self.modifier_theme)
        self.bouton_modifier.pack(padx=10, pady=5)

        self.bouton_supprimer = Button(self.frame, text="Supprimer le thème", command=self.supprimer_theme)
        self.bouton_supprimer.pack(padx=10, pady=5)

        self.listbox.bind("<<ListboxSelect>>", self.activer_boutons)  # Lie la sélection de la listebox à la méthode

        self.afficher_themes()

        self.fenetre.mainloop()

    def afficher_themes(self):
        """
        Affiche la liste des thèmes dans la listebox.
        """
        themes = self.db.lister_themes()
        self.listbox.delete(0, END)  # Efface les anciens éléments de la listebox

        for theme in themes:
            self.listbox.insert(END, theme)

    def ajouter_theme(self):
        """
        Permet à l'utilisateur d'ajouter un nouveau thème dans la listebox.
        """
        nouveau_theme = simpledialog.askstring("Ajouter un thème", "Nouveau thème :")

        if nouveau_theme:
            self.db.ajouter_theme(nouveau_theme)
            messagebox.showinfo("Thème ajouté", f"Le thème '{nouveau_theme}' a été ajouté.")
            self.afficher_themes()

    def modifier_theme(self):
        """
        Permet à l'utilisateur de modifier le thème sélectionné dans la listebox.
        """
        selected_theme = self.listbox.get(ACTIVE)

        if not selected_theme:
            return  # Sortir de la fonction si aucun thème n'est sélectionné

        nouveau_theme = simpledialog.askstring("Modifier le thème", "Nouveau thème :", initialvalue=selected_theme)

        if nouveau_theme:
            self.db.modifier_theme(selected_theme, nouveau_theme)
            messagebox.showinfo("Thème modifié", f"Le thème '{selected_theme}' a été modifié en '{nouveau_theme}'.")
            self.afficher_themes()

    def supprimer_theme(self):
        """
        Permet à l'utilisateur de supprimer le thème sélectionné dans la listebox.
        """
        selected_theme = self.listbox.get(ACTIVE)

        if not selected_theme:
            return  # Sortir de la fonction si aucun thème n'est sélectionné

        if messagebox.askokcancel("Confirmer la suppression", f"Êtes-vous sûr de vouloir supprimer le thème '{selected_theme}' ?"):
            self.db.supprimer_theme(selected_theme)
            messagebox.showinfo("Thème supprimé", f"Le thème '{selected_theme}' a été supprimé.")
            self.afficher_themes()

    def activer_boutons(self, event=None):
        """
        Active ou désactive les boutons en fonction de la sélection dans la listebox.
        """
        if self.listbox.curselection():
            self.bouton_modifier.config(state=NORMAL)
            self.bouton_supprimer.config(state=NORMAL)
        else:
            self.bouton_modifier.config(state=DISABLED)
            self.bouton_supprimer.config(state=DISABLED)

    def fermer_fenetre(self):
        """
        Ferme la fenêtre et ferme la connexion à la base de données.
        """
        self.db.fermer_connexion()
        self.fenetre.destroy()

if __name__ == "__main__":
    root = Tk()
    edition_themes = EditionThemes(root)
    root.mainloop()
