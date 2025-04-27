import sqlite3
import database_utils
import theses_management
import other_utils
import search_utils
from class_utils import Thesis


def main():
    
    # Tenter de se reconnecter en cas d'échec de connexion à theses.fr
    http = other_utils.config_strategy()

    # Connexion à la base de données SQLite et création du curseur
    conn = sqlite3.connect('theses.db')
    cursor = conn.cursor()


    # Parcours les personnes de la base de données non processed
    while True :
        cursor.execute("SELECT ppn, nom, prenom  FROM personnes WHERE processed = 0 LIMIT 1")
        result = cursor.fetchone()

        if result is None : # Plus personne à traiter
            break

        ppn, nom, prenom = result

        # Récupère la thèse de la personne
        phd_dict = search_utils.find_thesis_by_ppn(http, ppn, nom, prenom)

        # S'il y a une thèse
        if phd_dict != False :

            # Transforme les données dictionnaire en object
            phd = Thesis(phd_dict)

            # Si la personne a fait une thèse en astro, update la database
            theses_management.add_author_thesis_and_supervisor(cursor, phd)


        # Récupère les thèses encadrées par la personne
        list_phd_dict = search_utils.find_supervised_theses_by_name(http, ppn, nom, prenom)

        # S'il y a une thèse encadrée
        if list_phd_dict != False :

            for phd_dict in list_phd_dict :

                # Transforme les données dictionnaire en object
                phd = Thesis(phd_dict)

                # Si la personne a fait une thèse en astro, rajoute juste l'auteur sans processed
                theses_management.add_person_if_not_exists(cursor, phd.ppn, phd.nom, phd.prenom, phd.thesis_id)




        # Marque la personne comme 'processed'
        database_utils.mark_as_processed(cursor, ppn)

        # Sauvegarder les changements
        conn.commit()
    
    # Fermer la connexion
    conn.close()

main()
print("End")