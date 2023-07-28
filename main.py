from tkinter import Tk
from PenduJeuGraphique import PenduJeuGraphique
from PenduJeuLogique import PenduJeuLogique

if __name__ == "__main__":
    fenetre = Tk()
    
    # Partie graphique
    app_graphique = PenduJeuGraphique(fenetre)

    # Partie logique
    app_logique = PenduJeuLogique(fenetre)
    app_logique.fenetre.protocol("WM_DELETE_WINDOW", app_logique.fermer_fenetre)

    fenetre.mainloop()
