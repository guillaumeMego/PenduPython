from tkinter import *

class PenduSvg:
    """
    Classe pour tracer le pendu.

    Attributes:
        canvas (Canvas): Le canvas sur lequel tracer le pendu.
        mots_faux (list): Liste des lettres incorrectes proposées.
    """
    base_du_pendu = 120, 40, 120, 440
    poutre_maintien = 40, 440, 200, 440
    barre_horizontale = 120, 40, 280, 40
    corde = 280, 40, 280, 80
    tete_du_pendu = 240, 80, 320, 160
    corps = 280, 160, 280, 280
    bras_droit = 280, 200, 320, 240
    bras_gauche = 280, 200, 240, 240
    jambe_gauche = 280, 280, 240, 400
    jambe_droite = 280, 280, 320, 400

    def __init__(self, canvas):
        self.canvas = canvas
        self.mots_faux = []

    def tracer(self): 
        """
        Trace le pendu en fonction du nombre de lettres incorrectes proposées.
        """
        if len(self.mots_faux) == 1:
            self.canvas.create_line(*self.poutre_maintien, width=5)
        elif len(self.mots_faux) == 2:
            self.canvas.create_line(*self.base_du_pendu, width=5)
        elif len(self.mots_faux) == 3:
            self.canvas.create_line(*self.barre_horizontale, width=5)
        elif len(self.mots_faux) == 4:
            self.canvas.create_line(*self.corde, width=5)
        elif len(self.mots_faux) == 5:
            self.canvas.create_oval(*self.tete_du_pendu, width=5)
        elif len(self.mots_faux) == 6:
            self.canvas.create_line(*self.corps, width=5)
        elif len(self.mots_faux) == 7:
            self.canvas.create_line(*self.bras_droit, width=5)
        elif len(self.mots_faux) == 8:
            self.canvas.create_line(*self.bras_gauche, width=5)
        elif len(self.mots_faux) == 9:
            self.canvas.create_line(*self.jambe_gauche, width=5)
        elif len(self.mots_faux) == 10:
            self.canvas.create_line(*self.jambe_droite, width=5)
        
        if self.verifier_partie_perdue():
            self.canvas.delete("all")
            self.canvas.create_text(280, 420, text="👎", font=("Helvetica", 75))

    def verifier_partie_perdue(self):
        """
        Vérifie si la partie est perdue (toutes les parties du corps tracées).
        """
        return len(self.mots_faux) == 10

    def ajouter_mot_faux(self, lettre):
        """
        Ajoute la lettre à la liste des lettres incorrectes proposées et trace le pendu.
        """
        if lettre not in self.mots_faux:
            self.mots_faux.append(lettre)
            self.tracer()

if __name__ == "__main__":
    fenetre = Tk()
    fenetre.mainloop()