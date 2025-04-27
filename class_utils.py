from other_utils import clean_text
from other_utils import generate_unique_id

class Thesis:
    def __init__(self, phd):

        # Information sur la thèse
        self.thesis_id = phd["id"]
        self.thesis_title = clean_text(phd["titrePrincipal"])
        if phd["dateSoutenance"] is not None :
            self.thesis_year = phd["dateSoutenance"][-4:]
        else :
            self.thesis_year = str(int(phd["datePremiereInscriptionDoctorat"][-4:])+3)

        # Information sur l'auteur
        auteur = phd["auteurs"][0]
        self.nom = clean_text(auteur["nom"])
        self.prenom = clean_text(auteur["prenom"])
        if auteur["ppn"] is not None :
            self.ppn = auteur["ppn"]
        else :      # Génère un identifiant unique
            self.ppn = generate_unique_id(self.nom, self.prenom, self.thesis_title)

        # Information sur les superviseurs
        list_ppn_superviseur, list_nom_superviseur, list_prenom_superviseur = [], [], []
        for directeur in phd["directeurs"] :
            list_nom_superviseur.append(clean_text(directeur["nom"]))
            list_prenom_superviseur.append(clean_text(directeur["prenom"]))

            if directeur["ppn"] is not None :
                list_ppn_superviseur.append(directeur["ppn"])
            else :      # Génère un identifiant unique
                unique_id = generate_unique_id(clean_text(directeur["nom"]), clean_text(directeur["prenom"]), self.thesis_title)
                list_ppn_superviseur.append(unique_id)

            list_ppn_superviseur.append(directeur["ppn"])

        self.list_ppn_superviseur = list_ppn_superviseur
        self.list_nom_superviseur = list_nom_superviseur
        self.list_prenom_superviseur = list_prenom_superviseur

    def show(self):
        print(f"Auteur: {self.nom} {self.prenom} (PPN: {self.ppn})")
        print(f"id: {self.thesis_id}")
        print(f"Titre: {self.thesis_title}")
        print(f"Année: {self.thesis_year}")
        print("Superviseurs:")
        for ppn, nom, prenom in zip(self.list_ppn_superviseur, self.list_nom_superviseur, self.list_prenom_superviseur):
            print(f" - {nom} {prenom} (PPN: {ppn})")



