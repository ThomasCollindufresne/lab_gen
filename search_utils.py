import other_utils



def find_thesis_by_ppn(http, ppn, nom, prenom):

    # Si le ppn ne provient pas de theses.fr
    if len(ppn) == 9 :
        url = f"https://theses.fr/api/v1/theses/recherche/?q=auteursPpn:({ppn})&nombre=100"
    elif len(ppn) == 64 :
        url = f"https://theses.fr/api/v1/theses/recherche/?q=auteursNP:({prenom} {nom})&nombre=100"


    # Récupérer les thèses
    response = http.get(url)

    # Check le status de la réponse
    if response.status_code != 200:
        input(f"Soucis lors de la recherche de thèse de {ppn} !\nResponse status code : {response.status_code}")
        return(False)

    # Récupérer les données
    data = response.json()

    # Si aucune thèse trouvée, False
    if data['totalHits'] == 0 :
        return False
        
    # Sinon
    else :
        list_phd = []
        for phd in data['theses'] :
            # Vérifier si la thèse est en astro
            if other_utils.is_phd_in_astro(phd) :
                list_phd.append(phd)
        
        if len(list_phd) > 0 :
            return(list_phd[0]) # Si plusieurs thèses en astro, tant pis, renvoie que la premiere
        elif len(list_phd) == 0 :
            return(False)















def find_supervised_theses_by_name(http, ppn, nom, prenom):

    # Récupérer les thèses
    if len(ppn) == 9 :      # Si le ppn provient de theses.fr
        url = f"https://theses.fr/api/v1/theses/recherche/?q=directeursPpn:({ppn})&nombre=100"
    elif len(ppn) == 64 :   # Si le ppn ne provient pas de theses.fr
        url = f"https://theses.fr/api/v1/theses/recherche/?q=directeursNP:({prenom} {nom})&nombre=100"

    response = http.get(url)

    # Check le status de la réponse
    if response.status_code != 200:
        input(f"Soucis lors de la recherche de thèse de {ppn} !\nResponse status code : {response.status_code}")
        return(False)

    # Récupérer les données
    data = response.json()

    # Si aucune thèse encadrée, False
    if data['totalHits'] == 0 :
        return(False)

    # Sinon
    else :
        
        # Liste des thèses encadrées via ppn, en astro
        list_phd = []

        # Pour chaque thèse :
        for phd in data['theses'] :
            
            # Si la thèse est en astro
            if other_utils.is_phd_in_astro(phd) :
                list_phd.append(phd)
        
        if len(list_phd) > 0 :
            return(list_phd)
        
        else :
            return(False)
