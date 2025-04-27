import sqlite3


# Connexion à la base de données SQLite (création du fichier thèses.db si il n'existe pas)
conn = sqlite3.connect("theses.db")


# Création d'un curseur pour exécuter les requêtes SQL
cursor = conn.cursor()


# Création de la table 'personnes' pour stocker les informations des auteurs et superviseurs
cursor.execute("""
    CREATE TABLE IF NOT EXISTS personnes (
        ppn TEXT PRIMARY KEY,
        nom TEXT,
        prenom TEXT,
        processed INTEGER DEFAULT 0
    )
""")

# Création de la table 'theses' pour stocker les informations des thèses
cursor.execute("""
    CREATE TABLE IF NOT EXISTS theses (
        thesis_id TEXT PRIMARY KEY,
        titre TEXT,
        annee INTEGER,
        auteur_ppn TEXT,
        FOREIGN KEY(auteur_ppn) REFERENCES personnes(ppn)
    )
""")

# Création de la table 'superviseurs' pour relier les superviseurs aux thèses
cursor.execute("""
    CREATE TABLE IF NOT EXISTS superviseurs (
        supervisor_ppn TEXT,
        thesis_id TEXT,
        FOREIGN KEY(supervisor_ppn) REFERENCES personnes(ppn),
        FOREIGN KEY(thesis_id) REFERENCES theses(thesis_id)
    )
""")



# Ajoute une première personne comme base
ppn = "154852171"
nom = "Gratier"
prenom = "Pierre"
cursor.execute("""INSERT INTO personnes (ppn, nom, prenom) VALUES (?, ?, ?)""",
               (ppn, nom, prenom))




# Sauvegarder les changements dans la base de données
conn.commit()
