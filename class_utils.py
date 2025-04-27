from other_utils import clean_text


class Thesis:
    def __init__(self, phd):

        # Information sur la thèse
        self.thesis_id = phd["id"]
        self.thesis_title = clean_text(phd["titrePrincipal"])
        self.thesis_year = phd["dateSoutenance"][-4:]

        # Information sur l'auteur
        auteur = phd["auteurs"][0]
        self.ppn = auteur["ppn"]
        self.nom = clean_text(auteur["nom"])
        self.prenom = clean_text(auteur["prenom"])

        # Information sur les superviseurs
        list_ppn_superviseur, list_nom_superviseur, list_prenom_superviseur = [], [], []
        for directeur in phd["directeurs"] :
            list_ppn_superviseur.append(directeur["ppn"])
            list_nom_superviseur.append(clean_text(directeur["nom"]))
            list_prenom_superviseur.append(clean_text(directeur["prenom"]))
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



