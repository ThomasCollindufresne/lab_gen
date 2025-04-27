# database_utils.py
import sqlite3


# Fonction pour vérifier si une personne existe
def person_exists(cursor, ppn):
    cursor.execute("""SELECT ppn, processed FROM personnes WHERE ppn = ?""", (ppn,))
    return cursor.fetchone()

# Fonction pour vérifier si une thèse existe
def thesis_exists(cursor, thesis_id):
    cursor.execute("""SELECT thesis_id FROM theses WHERE thesis_id = ?""", (thesis_id,))
    return cursor.fetchone()



# Fonction pour ajouter une personne
def add_person(cursor, ppn, nom, prenom):
    cursor.execute("""INSERT INTO personnes (ppn, nom, prenom) VALUES (?, ?, ?)""", (ppn, nom, prenom))

# Fonction pour ajouter une thèse
def add_thesis(cursor, thesis_id, thesis_title, thesis_year, auteur_ppn):
    cursor.execute("""INSERT INTO theses (thesis_id, titre, annee, auteur_ppn) VALUES (?, ?, ?, ?)""", (thesis_id, thesis_title, thesis_year, auteur_ppn))
    return cursor.lastrowid

# Fonction pour ajouter un superviseur à une thèse
def add_supervisor(cursor, supervisor_ppn, thesis_id):
    cursor.execute("""INSERT INTO superviseurs (supervisor_ppn, thesis_id) VALUES (?, ?)""", (supervisor_ppn, thesis_id))



# Fonction pour mettre à jour le champ 'processed' de la personne
def mark_as_processed(cursor, ppn):
    cursor.execute("""UPDATE personnes SET processed = 1 WHERE ppn = ?""", (ppn,))
