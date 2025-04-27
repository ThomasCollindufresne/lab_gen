import sqlite3
import database_utils
import theses_management

def main():
    
    # Connexion à la base de données SQLite et création du curseur
    conn = sqlite3.connect('theses.db')
    cursor = conn.cursor()

    # Données de Pierre Gratier et Jonathan Braine
    ppn = "154852171"
    nom = "Gratier"
    prenom = "Pierre"
    thesis_id = "2010BOR14083"
    thesis_title = "Étude du milieu interstellaire de galaxies chimiquement jeunes du Groupe Local"
    thesis_year = 2010

    list_ppn_superviseur = ["123456789" ]   # PPN de Jonathan Braine (à titre d'exemple)
    list_nom_superviseur = ["Braine"]
    list_prenom_superviseur = ["Jonathan"]

    # 1. Ajouter la personne Pierre Gratier si elle n'est pas déjà dans la base de données
    if theses_management.add_person_if_not_exists(cursor, ppn, nom, prenom):
        # 2. Ajouter la thèse et le superviseur si la thèse n'existe pas déjà
        theses_management.add_thesis_and_supervisor(cursor, ppn, nom, prenom, list_ppn_superviseur, list_nom_superviseur, list_prenom_superviseur, thesis_id, thesis_title, thesis_year)

    # Sauvegarder les changements
    conn.commit()
    
    # Fermer la connexion
    conn.close()

main()
