from tkinter import *
from PenduApparence import PenduApparence
from PenduSvg import PenduSvg
from PenduMenu import PenduMenu
from PenduJeuLogique import PenduJeuLogique

class PenduJeuGraphique(PenduJeuLogique):
    """
    Classe pour le jeu du pendu en mode graphique.
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
        super().__init__(fenetre)

        # Créer le canvas avec fond beige et sans padding
        self.canvas = Canvas(self.fenetre, width=500, bg='beige')
        self.canvas.grid(row=0, column=0, sticky="nsew")

        # Créer un frame pour l'alphabet et le mot
        self.frame_alphabet = Frame(self.fenetre)
        self.frame_alphabet.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        # Ajuster la répartition de l'espace en utilisant grid_rowconfigure et grid_columnconfigure
        self.fenetre.grid_rowconfigure(0, weight=1)
        self.fenetre.grid_columnconfigure(0, weight=3)
        self.fenetre.grid_columnconfigure(1, weight=7)

        # Créer une instance de PenduMenu avec la fenêtre et self comme arguments
        self.menu_creator = PenduMenu(self.fenetre, self)
        self.menu_creator.create_menu()

        # Créer une instance de PenduApparence avec le canvas et self.nouvelle_partie comme arguments
        self.apparence = PenduApparence(self.frame_alphabet, self.proposer_lettre, self.nouvelle_partie, self.canvas)

        # Créer une frame pour les tirets et les centrer
        self.frame_tirets = Frame(self.frame_alphabet)
        self.frame_tirets.grid(row=1, column=1, padx=10, pady=70)

        # Créer un label pour les tirets et le centrer
        self.label_mot = Label(self.frame_tirets, text="", font=("Helvetica", 40), anchor="center")
        self.label_mot.grid(row=1, column=1, padx=10, pady=70)

        # Créer une instance de PenduSvg avant d'appeler choisir_nouvelle_partie()
        self.pendu = PenduSvg(self.canvas)
    

if __name__ == "__main__":
    fenetre = Tk()
    app_graphique = PenduJeuGraphique(fenetre)
    fenetre.protocol("WM_DELETE_WINDOW", app_graphique.fermer_fenetre)
    fenetre.mainloop()
