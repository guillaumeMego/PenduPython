from tkinter import *

class PenduApparence:
    """
    Classe pour l'apparence du jeu du pendu.
    Attributes:
        fenetre (Tk): La fenêtre principale du jeu.
        proposer_lettre (function): La fonction pour proposer une lettre.
        nouvelle_partie (function): La fonction pour choisir une nouvelle partie.
        canvas (Canvas): Le canvas sur lequel tracer le pendu.
        mot_actuel (str): Le mot actuel avec les lettres trouvées.
        frame_gauche (Frame): Le frame pour le contenu à gauche.
        frame_droit (Frame): Le frame pour le contenu à droite.
        label_mot (Label): Le label pour le mot actuel.
    """
    def __init__(self, fenetre, proposer_command, nouvelle_partie_command, canvas):
        self.fenetre = fenetre
        self.proposer_lettre = proposer_command
        self.nouvelle_partie = nouvelle_partie_command
        self.canvas = canvas

        self.mot_actuel = ""

        # Créer deux frames pour le contenu à gauche et à droite
        self.frame_gauche = Frame(fenetre)
        self.frame_droit = Frame(fenetre)

        self.frame_gauche.grid(row=0, column=0, padx=10, pady=10)
        self.frame_droit.grid(row=0, column=1, padx=10, pady=10)

        self.label_mot = Label(self.frame_gauche, text="", font=("Helvetica", 20))
        self.label_mot.pack()

        # Convertir l'utilisation de pack en grid pour les widgets existants dans self.frame_droit
        self.frame_droit.pack_forget()
        self.frame_droit.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.creer_alphabet()

    def creer_alphabet(self):
        """
        Crée les boutons pour les lettres de l'alphabet.
        """
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i in range(3):
            ligne_alphabet = alphabet[i * 10: (i + 1) * 10]
            for j, lettre in enumerate(ligne_alphabet):
                bouton_lettre = Button(self.frame_droit, text=lettre, command=lambda l=lettre: self.proposer_lettre(l))
                bouton_lettre.grid(row=i, column=j, padx=2, pady=2)  # Utiliser grid au lieu de pack

                bouton_lettre.config(width=2, height=2, font=("Helvetica", 20),
                                    bg="lightblue", 
                                    activebackground="blue", 
                                    activeforeground="white", 
                                    relief=RAISED, 
                                    bd=5)
    
    def griser_bouton(self, lettre):
        """
        Grise le bouton de la lettre proposée.
        """
        for bouton in self.frame_droit.winfo_children():
            if bouton["text"] == lettre:
                bouton.config(state=DISABLED)

    def effacer_bouton(self, lettre):
        """
        Efface le bouton de la lettre proposée.
        """
        for bouton in self.frame_droit.winfo_children():
            if bouton["text"] == lettre:
                bouton.destroy()
    
    def afficher_mot_actuel(self, mot_actuel):
        """
        Affiche le mot actuel avec les lettres trouvées.
        """
        self.label_mot.config(text=" ".join(mot_actuel))

    def cacher_clavier(self):
        """
        Cache tous les boutons du clavier.
        """
        for bouton in self.frame_droit.winfo_children():
            bouton.grid_remove()

if __name__ == "__main__":
    fenetre = Tk()
    apparence = PenduApparence(fenetre, lambda x: print(x), lambda x: print(x), Canvas(fenetre))
    fenetre.mainloop()