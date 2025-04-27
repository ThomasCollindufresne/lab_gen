import other_utils



def find_thesis_by_ppn(http, ppn):

    # Récupérer les thèses soutenues via le ppn 
    url = f"https://theses.fr/api/v1/theses/recherche/?q=auteursPpn:({ppn})&nombre=100"
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

    # Si plus d'une thèse trouvée, Error 
    elif data['totalHits'] > 1 :
         raise ValueError("Vérifier si c'est normal que la personne possède 2 thèses pour un même ppn")
         
    # Si une unique thèse trouvée
    else :
        # Vérifier si la thèse est en astro
        phd = data['theses'][0]
        if other_utils.is_phd_in_astro(phd) :
            return(phd)

    return(False)














def find_supervised_theses_by_name(http, ppn):

    # Récupérer les thèses encadrées via le ppn 
    url = f"https://theses.fr/api/v1/theses/recherche/?q=directeursPpn:({ppn})&nombre=100"
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
        for i, phd in enumerate(data['theses']) :
            
            # Si la thèse est en astro
            if other_utils.is_phd_in_astro(phd) :
                list_phd.append(phd)

    return(False)
