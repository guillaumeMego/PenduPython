import random
from tkinter import *
from tkinter import messagebox
from PenduSvg import PenduSvg
from PenduMenu import PenduMenu
from PenduDb import PenduDb
from PenduApparence import PenduApparence

class PenduJeuLogique:
    """
    Classe pour le jeu du pendu en mode logique.
    Attributes:
        fenetre (Tk): La fenêtre principale du jeu.
        canvas (Canvas): Le canvas sur lequel tracer le pendu.
        frame_alphabet (Frame): Le frame pour l'alphabet et le mot.
        menu_creator (PenduMenu): L'instance de PenduMenu.
        apparence (PenduApparence): L'instance de PenduApparence.
        frame_tirets (Frame): Le frame pour les tirets.
        label_mot (Label): Le label pour le mot.
        pendu (PenduSvg): L'instance de PenduSvg.
    """
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.fenetre.title("Jeu du pendu")
        self.pendu = None 
        self.mots_du_theme = [] 
        self.mot_secret = ""
        self.mot_actuel = []
        self.nb_chances = 10 
        self.db = None
        self.themes = []
        self.theme_choisi = None


    def mettre_a_jour_theme_selectionne(self, theme):
        """
        Met à jour le thème sélectionné.
        """
        self.theme_choisi = theme
        self.choisir_nouvelle_partie()

    def choisir_nouvelle_partie(self, theme_choisi=None):
        """
        Choisis un nouveau mot secret et réinitialise le jeu.
        """
        self.db = PenduDb()  
        self.db.create_db()

        self.themes = self.db.lister_themes()  

        if theme_choisi and theme_choisi in self.themes:
            self.theme_choisi = theme_choisi
        else:
            self.theme_choisi = random.choice(self.themes)

        self.mots_du_theme = self.db.lister_mots_par_theme(self.theme_choisi)
        self.nouvelle_partie()

    def proposer_lettre(self, lettre):
        """
        Propose une lettre et vérifie si elle est dans le mot secret.
        """
        lettre = lettre.lower()
        if lettre.isalpha() and len(lettre) == 1:
        
            if lettre in self.mot_secret:
                self.mot_actuel = self.verifier_lettre(lettre, self.mot_secret, self.mot_actuel)
                self.apparence.effacer_bouton(lettre.upper())
                self.afficher_mot_actuel()

                if "_" not in self.mot_actuel:
                    self.partie_gagnee()
            else:
                self.pendu.ajouter_mot_faux(lettre)
                self.apparence.griser_bouton(lettre.upper())

                if PenduSvg.verifier_partie_perdue(self.pendu):
                    self.apparence.cacher_clavier()
                    messagebox.showinfo("Partie perdue", f"Dommage ! Vous avez perdu la partie. Le mot secret était : {self.mot_secret}.")
                    self.nouvelle_partie()
        else:
            messagebox.showwarning("Erreur", "Veuillez entrer une seule lettre de l'alphabet.")

    def verifier_lettre(self, lettre, mot_secret, mot_actuel):
        """
        Vérifie si la lettre proposée est dans le mot secret et met à jour le mot actuel.
        """
        mot_secret_list = list(mot_secret)
        for i, char in enumerate(mot_secret_list):
            if char == lettre:
                mot_actuel[i] = char
        return mot_actuel

    def afficher_mot_actuel(self):
        """
        Affiche le mot actuel.
        """
        self.label_mot.config(text=" ".join(self.mot_actuel))

    def nouvelle_partie(self):
        """
        Choisis un nouveau mot secret et réinitialise le jeu.
        """
        self.canvas.delete("all")
        self.apparence = PenduApparence(self.frame_alphabet, self.proposer_lettre, self.verifier_lettre, self.canvas)

        self.pendu.mots_faux = []

        self.mot_secret = random.choice(self.mots_du_theme)
        self.mot_actuel = ["_" if char.isalpha() else char for char in self.mot_secret]

        self.afficher_mot_actuel()  
        self.nb_chances = 10 

    def partie_gagnee(self):
        """
        Affiche un message de partie gagnée et propose une nouvelle partie.
        """
        self.canvas.delete("all")
        self.canvas.create_text(280, 420, text="👍", font=("Helvetica", 95))
        self.apparence.cacher_clavier()
        messagebox.showinfo("Partie Gagnée", f"Bravo ! Vous avez gagné la partie. Le mot secret était : {self.mot_secret}")
        self.nouvelle_partie()

    def fermer_fenetre(self):
        """
        Ferme la fenêtre.
        """
        self.fenetre.destroy()

if __name__ == "__main__":
    fenetre = Tk()
    app_logique = PenduJeuLogique
