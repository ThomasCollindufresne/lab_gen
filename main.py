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
        cursor.execute("SELECT ppn FROM personnes WHERE processed = 0 LIMIT 1")
        result = cursor.fetchone()

        if result is None : # Plus personne à traiter
            break

        ppn = result[0]

        # Récupère la thèse de la personne
        phd_dict = search_utils.find_thesis_by_ppn(http, ppn)

        # Si pas de thèse, on passe à l'itération d'après
        if phd_dict == False :
            database_utils.mark_as_processed(cursor, ppn)
            continue

        # Transforme les données dictionnaire en object
        phd = Thesis(phd_dict)

        # Si la personne a fait une thèse en astro, update la database
        theses_management.add_author_thesis_and_supervisor(cursor, phd)



    # Rajouter, sous forme de nouveaux auteurs, les personnes encadrées par ppn
    pass







    # Sauvegarder les changements
    conn.commit()
    
    # Fermer la connexion
    conn.close()

main()
