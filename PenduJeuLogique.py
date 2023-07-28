import random
from tkinter import *
from tkinter import messagebox
from PenduSvg import PenduSvg
from PenduMenu import PenduMenu
from PenduDb import PenduDb
from PenduApparence import PenduApparence

class PenduJeuLogique:
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.pendu = None 
        self.mots_du_theme = [] 
        self.mot_secret = ""
        self.mot_actuel = []
        self.nb_chances = 10 
        self.db = None
        self.themes = []
        self.theme_choisi = None

        

    def mettre_a_jour_theme_selectionne(self, theme):
        self.theme_choisi = theme
        self.choisir_nouvelle_partie()

    def choisir_nouvelle_partie(self, theme_choisi=None):
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
        mot_secret_list = list(mot_secret)
        for i, char in enumerate(mot_secret_list):
            if char == lettre:
                mot_actuel[i] = char
        return mot_actuel

    def afficher_mot_actuel(self):
        self.label_mot.config(text=" ".join(self.mot_actuel))

    def nouvelle_partie(self):
        self.canvas.delete("all")
        self.apparence = PenduApparence(self.frame_alphabet, self.proposer_lettre, self.verifier_lettre, self.canvas)

        self.pendu.mots_faux = []

        self.mot_secret = random.choice(self.mots_du_theme)
        self.mot_actuel = ["_" if char.isalpha() else char for char in self.mot_secret]

        self.afficher_mot_actuel()  
        self.nb_chances = 10 

    def partie_gagnee(self):
        self.canvas.delete("all")
        self.canvas.create_text(280, 420, text="👍", font=("Helvetica", 95))
        self.apparence.cacher_clavier()
        messagebox.showinfo("Partie Gagnée", f"Bravo ! Vous avez gagné la partie. Le mot secret était : {self.mot_secret}")
        self.nouvelle_partie()

    def fermer_fenetre(self):
        self.fenetre.destroy()

if __name__ == "__main__":
    fenetre = Tk()
    app_logique = PenduJeuLogique
