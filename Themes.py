from tkinter import *
from PenduDb import PenduDb
from tkinter import messagebox

class Themes:
    """
    Classe pour choisir un thème.
    Attributes:
        fenetre (Tk): La fenêtre principale du choix de theme.
        theme_selectionne (str): Le thème sélectionné.
    """
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.fenetre.title("Thèmes")
        self.fenetre.resizable(False, False)
        self.fenetre.protocol("WM_DELETE_WINDOW", self.fermer_fenetre)
        self.fenetre.geometry("400x400")

        self.theme_selectionne = ""  # Ajout de l'attribut theme_selectionne avec une valeur par défaut

        self.frame = Frame(self.fenetre)
        self.frame.pack(padx=10, pady=10)

        self.label = Label(self.frame, text="Choisissez un thème")
        self.label.pack(padx=10, pady=10)

        self.listbox = Listbox(self.frame)
        self.listbox.pack(padx=10, pady=10)

        self.bouton = Button(self.frame, text="Choisir", command=self.choisir_theme)
        self.bouton.pack(padx=10, pady=10)

        self.label.pack(padx=10, pady=10)
        self.listbox.pack(padx=10, pady=10)
        self.bouton.pack(padx=10, pady=10)

        self.charger_themes()

    def charger_themes(self):
        """
        Charge les thèmes depuis la base de données pendu.db et les affiche dans la liste.
        """
        self.db = PenduDb() 
        themes = self.db.lister_themes() 

        for theme in themes:
            self.listbox.insert(END, theme)

        self.listbox.bind("<<ListboxSelect>>", self.choisir_theme)

    def fermer_fenetre(self):
        """
        Ferme la fenêtre et renvoie le thème sélectionné.
        """
        if not hasattr(self, 'theme_selectionne'):
            self.theme_selectionne = ""
        self.fenetre.destroy()

    def choisir_theme(self):
        """
        Récupère le thème sélectionné et ferme la fenêtre.
        """
        selected_theme = self.listbox.get(self.listbox.curselection())

        if selected_theme:
            self.theme_selectionne = selected_theme 
            self.fermer_fenetre()  
            return selected_theme
        else:
            messagebox.showerror("Erreur", "Veuillez sélectionner un thème.")

if __name__ == "__main__":
    fenetre = Tk()
    themes = Themes(fenetre)
    fenetre.mainloop()