import sqlite3
import networkx as nx
import matplotlib.pyplot as plt

# Connexion à ta base de données
conn = sqlite3.connect('theses.db')
cursor = conn.cursor()


# Création du graphe orienté
G = nx.DiGraph()

# Récupérer toutes les thèses et leurs auteurs
cursor.execute("""
    SELECT theses.thesis_id, theses.auteur_ppn
    FROM theses
""")
theses = cursor.fetchall()

# Pour chaque thèse, ajouter des liens auteur -> superviseur
for thesis_id, auteur_ppn in theses:
    # Récupérer les superviseurs associés à la thèse
    cursor.execute("""
        SELECT supervisor_ppn
        FROM superviseurs
        WHERE thesis_id = ?
    """, (thesis_id,))
    superviseurs = cursor.fetchall()

    # Ajouter des arêtes du l'auteur vers chaque superviseur
    for (supervisor_ppn,) in superviseurs:
        if auteur_ppn and supervisor_ppn:
            G.add_edge(auteur_ppn, supervisor_ppn)

# Fermer la connexion
conn.close()

# Dessiner le graphe
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, k=0.5)  # Disposition des noeuds
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', arrows=True)
plt.title("Graph des auteurs et de leurs superviseurs")
plt.show()
