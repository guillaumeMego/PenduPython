from PenduDb import PenduDb
from tkinter import *
from tkinter import simpledialog, messagebox

class Edition:
    # edition des mots et des themes de la bdd
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.fenetre.title("Edition")
        self.fenetre.resizable(False, False)
        self.fenetre.protocol("WM_DELETE_WINDOW", self.fermer_fenetre)
        self.fenetre.geometry("400x400")

        self.db = PenduDb()  
        self.selected_theme = None 

        self.frame = Frame(self.fenetre)
        self.frame.pack(padx=10, pady=10)

        self.label = Label(self.frame, text="Choisissez un thème")
        self.label.pack(padx=10, pady=10)

        self.listbox = Listbox(self.frame)
        self.listbox.pack(padx=10, pady=10)

        self.bouton_choisir = Button(self.frame, text="Choisir", command=self.choisir_theme)
        self.bouton_choisir.pack(padx=10, pady=10)

        self.bouton_ajouter = Button(self.frame, text="Ajouter un mot", command=self.ajouter_mot)
        self.bouton_ajouter.pack(padx=10, pady=5)
        self.bouton_ajouter.pack_forget() 

        self.bouton_modifier = Button(self.frame, text="Modifier le mot", command=self.modifier_mot)
        self.bouton_modifier.pack(padx=10, pady=5)
        self.bouton_modifier.pack_forget()  

        self.bouton_supprimer = Button(self.frame, text="Supprimer le mot", command=self.supprimer_mot)
        self.bouton_supprimer.pack(padx=10, pady=5)
        self.bouton_supprimer.pack_forget()  

        self.listbox.bind("<<ListboxSelect>>", self.activer_boutons)  

        self.afficher_themes()

        self.fenetre.mainloop()

    def afficher_themes(self):
        """
        Affiche la liste des thèmes dans la listebox.
        """
        themes = self.db.lister_themes()
        self.listbox.delete(0, END)  

        for theme in themes:
            self.listbox.insert(END, theme)

    def choisir_theme(self):
        """
        Choisis un thème et affiche les mots correspondants.
        """
        self.selected_theme = self.listbox.get(ACTIVE)
        mots = self.db.lister_mots_par_theme(self.selected_theme)

        self.listbox.delete(0, END)  

        for mot in mots:
            self.listbox.insert(END, mot)

        self.bouton_choisir.pack_forget()

        self.bouton_ajouter.pack()
        self.bouton_modifier.pack()
        self.bouton_supprimer.pack()

    def ajouter_mot(self):
        """
        Permet à l'utilisateur d'ajouter un nouveau mot dans la listebox.
        """
        if not self.selected_theme:
            messagebox.showwarning("Aucun thème sélectionné", "Veuillez choisir un thème avant d'ajouter un mot.")
            return

        nouveau_mot = simpledialog.askstring("Ajouter un mot", "Nouveau mot :")

        if nouveau_mot:
            self.db.ajouter_mot(nouveau_mot, self.selected_theme)
            messagebox.showinfo("Mot ajouté", f"Le mot '{nouveau_mot}' a été ajouté dans le thème '{self.selected_theme}'.")
            self.fermer_fenetre()


    def modifier_mot(self):
        """
        Permet à l'utilisateur de modifier le mot sélectionné dans la listebox.
        """
        selected_mot = self.listbox.get(ACTIVE)

        if not selected_mot:
            return  

        nouveau_mot = simpledialog.askstring("Modifier le mot", "Nouveau mot :", initialvalue=selected_mot)

        if nouveau_mot:
            self.db.modifier_mot(selected_mot, nouveau_mot)
            messagebox.showinfo("Mot modifié", f"Le mot '{selected_mot}' a été modifié en '{nouveau_mot}'.")
            self.fermer_fenetre()

    def supprimer_mot(self):
        """
        Permet à l'utilisateur de supprimer le mot sélectionné dans la listebox.
        """
        selected_mot = self.listbox.get(ACTIVE)

        if not selected_mot:
            return 

        if messagebox.askokcancel("Confirmer la suppression", f"Êtes-vous sûr de vouloir supprimer le mot '{selected_mot}' ?"):
            self.db.supprimer_mot(selected_mot)
            messagebox.showinfo("Mot supprimé", f"Le mot '{selected_mot}' a été supprimé.")
            self.fermer_fenetre()

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
    edition = Edition(root)
    root.mainloop()

