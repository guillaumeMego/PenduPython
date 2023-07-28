import sqlite3

class PenduDb:
    """
    Classe permettant de gérer la base de données pendu.db.
    """
    def __init__(self):
        self.conn = sqlite3.connect('pendu.db')
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS themes (
                        id INTEGER PRIMARY KEY,
                        nom TEXT
                        )''')

        self.c.execute('''CREATE TABLE IF NOT EXISTS mots (
                        id INTEGER PRIMARY KEY,
                        mot TEXT,
                        theme_id INTEGER,
                        FOREIGN KEY (theme_id) REFERENCES themes(id)
                        )''')
        
        self.create_db()

    def ajouter_mot(self, mot, theme):
        """
        Ajoute un mot dans la base de données.
        """
        self.c.execute("SELECT id FROM themes WHERE nom=?", (theme,))
        theme_id = self.c.fetchone()

        if not theme_id:
            self.c.execute("INSERT INTO themes (nom) VALUES (?)", (theme,))
            theme_id = self.c.lastrowid
        else:
            theme_id = theme_id[0]

        self.c.execute("INSERT INTO mots (mot, theme_id) VALUES (?, ?)", (mot, theme_id))
        self.conn.commit()

    def supprimer_mot(self, mot):
        """
        Supprime un mot de la base de données.
        """
        self.c.execute("DELETE FROM mots WHERE mot=?", (mot,))
        self.conn.commit()

    def modifier_mot(self, ancien_mot, nouveau_mot):
        """
        Modifie un mot dans la base de données.
        """
        self.c.execute("UPDATE mots SET mot=? WHERE mot=?", (nouveau_mot, ancien_mot))
        self.conn.commit()


    def ajouter_theme(self, nom_theme):
        """
        Ajoute un thème dans la base de données.
        """
        self.c.execute("INSERT INTO themes (nom) VALUES (?)", (nom_theme,))
        self.conn.commit()

    def lister_mots_par_theme(self, theme):
        """
        Renvoie la liste des mots du thème spécifié.
        """
        self.c.execute("SELECT mot FROM mots JOIN themes ON mots.theme_id = themes.id WHERE themes.nom=?", (theme,))
        return [row[0] for row in self.c.fetchall()]

    def lister_themes(self):
        """
        Renvoie la liste des thèmes.
        """
        self.c.execute("SELECT nom FROM themes")
        return [row[0] for row in self.c.fetchall()]

    def fermer_connexion(self):
        """
        Ferme la connexion à la base de données.
        """
        self.conn.close()

    def create_db(self):
        """
        Crée la base de données et ajoute des thèmes et des mots par défaut.
        """
        themes_existant = self.lister_themes()

        if "Développeur" not in themes_existant:
            self.ajouter_theme("Développeur")

        if "Designer" not in themes_existant:
            self.ajouter_theme("Designer")

        if not self.lister_mots_par_theme("Développeur"):
            self.ajouter_mot("fonction", "Développeur")
            self.ajouter_mot("python", "Développeur")
            self.ajouter_mot("programmation", "Développeur")
            self.ajouter_mot("algorithmique", "Développeur")
            self.ajouter_mot("variable", "Développeur")

        if not self.lister_mots_par_theme("Designer"):
            self.ajouter_mot("graphisme", "Designer")
            self.ajouter_mot("couleur", "Designer")
            self.ajouter_mot("dessin", "Designer")
            self.ajouter_mot("typographie", "Designer")
            self.ajouter_mot("logo", "Designer")

