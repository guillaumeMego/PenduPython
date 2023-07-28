import tkinter as tk
import xml.etree.ElementTree as ET
from Themes import Themes
from tkinter import messagebox

class PenduMenu:
    """ 
    Classe pour créer le menu du jeu.
    Attributes:
        root (Tk): La fenêtre principale du jeu.
        parent (PenduJeu): L'instance de PenduJeu.
    """
    def __init__(self, root, parent):
        self.root = root
        self.parent = parent

    def create_menu(self):
        """
        Crée le menu à partir du fichier XML menu.xml.

        Le fichier XML contient une liste de catégories de menu, chacune avec une liste de liens.
        Chaque lien a un label et une commande.
        """
        menu_bar = tk.Menu(self.root)
        menus = self.parse_xml_file("menu.xml")

        for menu in menus:
            menu_categorie = tk.Menu(menu_bar, tearoff=0)
            for lien in menu.findall("lien"):
                label = lien.find("label").text
                command = lien.find("command").text
                menu_categorie.add_command(label=label, command=lambda cmd=command: self.handle_command(cmd))

            menu_bar.add_cascade(label=menu.attrib["categorie"], menu=menu_categorie)

        self.root.config(menu=menu_bar)

    def parse_xml_file(self, filename):
        """
        Analyse le fichier XML et renvoie la liste des éléments <menu>.
        """
        tree = ET.parse(filename)
        return tree.getroot().findall("menu")

    def handle_command(self, command):
        """
        Appelle la fonction correspondant à la commande.
        """
        if command == "themes":
            self.themes = Themes(tk.Toplevel(self.root))
            self.parent.mettre_a_jour_theme_selectionne(self.themes.theme_selectionne)

        if command == "a_propos":
            messagebox.showinfo("A propos", "Jeu du pendu\n\nProgramme sous licence GPL3")
        
        if hasattr(self.parent, command):
            func = getattr(self.parent, command)
            func()

if __name__ == "__main__":
    root = tk.Tk()
    menu_creator = PenduMenu(root, None)
    menu_creator.create_menu()
    root.mainloop()
