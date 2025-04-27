import sqlite3
import database_utils
import theses_management

def main():
    
    # Connexion à la base de données SQLite et création du curseur
    conn = sqlite3.connect('theses.db')
    cursor = conn.cursor()

    ### Scrap de theses.fr pour récupérer les données d'une personne de la database
    pass

    # Données de Pierre Gratier (temporaire)
    ppn = "154852171"
    nom = "Gratier"
    prenom = "Pierre"
    thesis_id = "2010BOR14083"
    thesis_title = "Étude du milieu interstellaire de galaxies chimiquement jeunes du Groupe Local"
    thesis_year = 2010
    list_ppn_superviseur = ["072315512" ]
    list_nom_superviseur = ["Braine"]
    list_prenom_superviseur = ["Jonathan"]

    # Retirer la casse du texte
    pass

    # Vérifier que la thèse est en astro
    pass

    # Vérifier si la personne est dans la base de donnée
    result = database_utils.person_exists(cursor, ppn)
    if result is None :              # Absent dans la base de donnée
        _, processed = result
        if processed is not 1 :     # Si la personne n'a pas encore été processed

            # Ajouter l'auteur, la thèse et le superviseur
            theses_management.add_author_thesis_and_supervisor(cursor, ppn, nom, prenom, list_ppn_superviseur, list_nom_superviseur, list_prenom_superviseur, thesis_id, thesis_title, thesis_year)



    # Rajouter, sous forme de nouveaux auteurs, les personnes encadrées par ppn
    pass







    # Sauvegarder les changements
    conn.commit()
    
    # Fermer la connexion
    conn.close()

main()
