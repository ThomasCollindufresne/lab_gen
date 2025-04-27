import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import unicodedata
import re



def config_strategy() :
    """
    Configure une strategie de connexion, pour retenter en cas d'echec et eviter que le code ne s'arrete en cours de route
    """
    # Configurer le retry avec un nombre de tentatives et une stratégie
    retry_strategy = Retry(
        total=60,  # Nombre de tentatives avant d'abandonner
        backoff_factor=1,  # Temps d'attente entre les tentatives
        status_forcelist=[500, 502, 503, 504],  # Re-essayer en cas d'erreur serveur
        allowed_methods=["GET"]
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    http = requests.Session()
    http.mount("https://", adapter)

    return(http)



def clean_text(text) :
    """
    Retire les majuscules et accents
    """
    text = text.lower()
    text = unicodedata.normalize('NFD', text)
    text = ''.join(c for c in text if unicodedata.category(c) != 'Mn')

    # Remplacements des caractères indésirables
    text = text.replace('-', ' ')  # Remplace les tirets par des espaces
    text = text.replace('_', ' ')  # Remplace les underscores par des espaces
    text = text.replace("’", "'")  # Normalise les apostrophes
    text = re.sub(r'[.,;:!?/\\]', ' ', text)  # Remplace la ponctuation par des espaces
    text = re.sub(r'\s+', ' ', text).strip()  # Remplace les espaces multiples par un seul

    return text





def is_phd_in_astro(phd) :

    # Pour la recherche automatique
    keywords = ["astrochimique", "astronom", "astrophysi", "proto-etoile", "etoile",
                "stellaire", "galaxie", "vent solaire", "vents solaire", "planetaire",
                "planete", "nuages moleculaire", "nuage moleculaire", "telescope",
                "blazar", "galactique", "disques d'accretion", "comete",
                "martienne", "cosmique", "naines brunes", "naine brune",
                "lentille gravitationnelle", "cosmologique", "lunes glacees",
                "mission juice", "rayonnement cosmique",
                "jupiter", "saturne", "uranus" "neptune"]

    phd_in_astro = False

    # Si un des keywords apparait la discipline
    discipline = clean_text(phd['discipline'])
    if any(keyword in discipline for keyword in keywords) :
        phd_in_astro = True

    # Si un des keywords apparait dans les sujets
    for sujet in phd['sujets'] :
        sujet = clean_text(sujet['libelle'])
        if any(keyword in sujet for keyword in keywords) :
            phd_in_astro = True

    # Si un des keywords apparait dans les sujets libres
    for sujetRameau in phd['sujetsRameau'] :
        sujetRameau = clean_text(sujetRameau['libelle'])
        if any(keyword in sujetRameau for keyword in keywords) :
            phd_in_astro = True

    # Si un des keywords apparait dans le titre --> thèse en astro
    title = clean_text(phd['titrePrincipal'])
    if any(keyword in title for keyword in keywords) :
        phd_in_astro = True

    """
    if not phd_in_astro :
        print(discipline)
        for sujet in phd['sujets']:
            print(clean_text(sujet['libelle']))
        for sujetRameau in phd['sujetsRameau']:
            print(clean_text(sujetRameau['libelle']))
        print(title)
    """

    return(phd_in_astro)