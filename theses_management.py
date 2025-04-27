import database_utils
import other_utils




def add_person_if_not_exists(cursor, ppn, nom, prenom):

    # Vérifier si la personne existe déjà
    result = database_utils.person_exists(cursor, ppn)
    
    # Si la personne n'existe pas
    if result is None:
        # On ajoute la personne à la database
        database_utils.add_person(cursor, ppn, nom, prenom)
        print(f"Personne {nom} {prenom} ajoutée.")







def add_author_thesis_and_supervisor(cursor, phd):
    
    # Ajouter la personne si elle n'existe pas
    add_person_if_not_exists(cursor, phd.ppn, phd.nom, phd.prenom)

    # Vérifier si la thèse existe déjà
    result = database_utils.thesis_exists(cursor, phd.thesis_id)
    
    # Si la thèse n'existe pas
    if result is None:
        # Ajouter la thèse à la database
        database_utils.add_thesis(cursor, phd.thesis_id, phd.thesis_title, phd.thesis_year, phd.ppn)
        print("Thèse ajoutée.")

        # Pour chaque superviseur
        for (ppn_superviseur, nom_superviseur, prenom_superviseur) in zip(phd.list_ppn_superviseur, phd.list_nom_superviseur, phd.list_prenom_superviseur):
            
            # Ajouter le superviseur à la thèse
            database_utils.add_supervisor(cursor, ppn_superviseur, phd.thesis_id)
            print(f"Superviseur {nom_superviseur} {prenom_superviseur} ajouté à la thèse.")

            # Ajouter le superviseur en temps que nouvelle personne qui n'a pas été processed
            add_person_if_not_exists(cursor, ppn_superviseur, nom_superviseur, prenom_superviseur)

        # Mettre à jour l'état de la personne comme "processed"
        database_utils.mark_as_processed(cursor, phd.ppn)
        print(f"L'auteur {phd.nom} {phd.prenom} a été processed.")

    else:
        print("La thèse existe déjà.")
