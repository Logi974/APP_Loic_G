"""
Module de persistance des formes - VERSION ÉTUDIANT.

EXERCICE 3 du laboratoire :
Implémenter les opérations CRUD pour stocker et relire les formes de
l'exercice 1 dans la base de données de l'exercice 2.

La fonction lister_formes() est FOURNIE comme exemple : étudiez-la pour
comprendre comment :
- ouvrir la connexion et obtenir un curseur;
- construire une requête SQL avec filtres optionnels;
- passer les valeurs avec des ? (jamais par interpolation de chaîne!).

Prérequis : avoir complété formes.py (exercice 1) et créé la base lab.db
avec formes_schema.sql et formes_donnees.sql (exercice 2).
"""

import sqlite3

from formes import Point, Rectangle, Cercle, Carre

DB_PATH = "lab.db"


def get_connection(db_path=DB_PATH):
    """
    Retourne une connexion à la base de données.

    FONCTION FOURNIE. La connexion est configurée pour donner accès aux
    colonnes par leur nom (row["categorie"] plutôt que row[2]).
    """
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


def lister_formes(dessin_id=None, categorie=None, db_path=DB_PATH):
    """
    Liste les formes avec filtres optionnels.

    FONCTION FOURNIE comme exemple de requête SELECT.

    Args:
        dessin_id: Filtre par dessin (optionnel)
        categorie: Filtre par catégorie (optionnel)
        db_path: Chemin vers la base de données

    Returns:
        Liste de rangées (sqlite3.Row)
    """
    conn = get_connection(db_path)
    try:
        cursor = conn.cursor()

        query = "SELECT * FROM formes WHERE 1=1"
        params = []

        if dessin_id is not None:
            query += " AND dessin_id = ?"
            params.append(dessin_id)

        if categorie is not None:
            query += " AND categorie = ?"
            params.append(categorie)

        query += " ORDER BY forme_id"

        cursor.execute(query, params)
        return cursor.fetchall()
    finally:
        conn.close()


def ajouter_forme(dessin_id, forme, db_path=DB_PATH):
    """
    Ajoute une forme (un objet de formes.py) dans la base de données.

    TODO 1: À IMPLÉMENTER

    Instructions :
    1. Déterminer la catégorie et les colonnes à remplir selon le type de
       l'objet, avec isinstance(forme, ...) :
       - Carre     -> categorie 'carre',     largeur et hauteur
       - Rectangle -> categorie 'rectangle', largeur et hauteur
       - Cercle    -> categorie 'cercle',    rayon
       ATTENTION : testez Carre AVANT Rectangle. Pourquoi ?
       (Indice : un Carre EST un Rectangle...)
    2. Exécuter l'INSERT avec des ? pour toutes les valeurs; les colonnes
       non pertinentes restent NULL.
    3. Appeler conn.commit() pour rendre l'insertion permanente.
    4. Retourner cursor.lastrowid (le forme_id généré).

    Args:
        dessin_id: Identifiant du dessin auquel la forme appartient
        forme: Objet Rectangle, Carre ou Cercle
        db_path: Chemin vers la base de données

    Returns:
        forme_id de la forme créée
    """
    # TODO: Implémenter cette fonction
    pass


def lire_forme(forme_id, db_path=DB_PATH):
    """
    Récupère une forme par son ID et la reconstruit en objet de formes.py.

    TODO 2: À IMPLÉMENTER

    Instructions :
    1. Faire un SELECT avec WHERE forme_id = ? et récupérer la rangée
       avec cursor.fetchone().
    2. Si aucune rangée : retourner None.
    3. Construire le bon objet selon row["categorie"] :
       - 'carre'     -> Carre(centre, largeur)
       - 'rectangle' -> Rectangle(centre, largeur, hauteur)
       - 'cercle'    -> Cercle(centre, rayon)
       où centre = Point(row["centre_x"], row["centre_y"]).
    4. Retourner l'objet.

    Args:
        forme_id: Identifiant de la forme
        db_path: Chemin vers la base de données

    Returns:
        Objet Rectangle, Carre ou Cercle, ou None si non trouvé
    """
    # TODO: Implémenter cette fonction
    pass


def deplacer_forme(forme_id, dx, dy, db_path=DB_PATH):
    """
    Déplace une forme directement dans la base de données.

    TODO 3: À IMPLÉMENTER

    Instructions :
    1. Exécuter un UPDATE qui incrémente les colonnes :
       SET centre_x = centre_x + ?, centre_y = centre_y + ?
       (oui, on peut utiliser la valeur actuelle d'une colonne!)
    2. Ne pas oublier le WHERE... et le commit().
    3. Retourner True si cursor.rowcount > 0, False sinon.

    C'est l'équivalent SQL de la méthode deplacer() de l'exercice 1.

    Args:
        forme_id: Identifiant de la forme
        dx, dy: Déplacement en x et en y
        db_path: Chemin vers la base de données

    Returns:
        True si déplacée, False sinon
    """
    # TODO: Implémenter cette fonction
    pass


def supprimer_forme(forme_id, db_path=DB_PATH):
    """
    Supprime une forme.

    TODO 4: À IMPLÉMENTER

    Instructions :
    1. Exécuter DELETE FROM formes WHERE forme_id = ?, puis commit().
    2. Retourner True si cursor.rowcount > 0, False sinon.

    Args:
        forme_id: Identifiant de la forme
        db_path: Chemin vers la base de données

    Returns:
        True si supprimée, False sinon
    """
    # TODO: Implémenter cette fonction
    pass


# NOTES POUR LES ÉTUDIANTS:
#
# 1. Structure générale d'une fonction CRUD:
#    conn = get_connection(db_path)
#    try:
#        cursor = conn.cursor()
#        cursor.execute("SQL...", (params,))
#        conn.commit()              # pour INSERT, UPDATE, DELETE
#        return ...                 # lastrowid, objet, ou rowcount > 0
#    finally:
#        conn.close()
#
# 2. Les valeurs passent TOUJOURS par des ?, jamais par des f-strings.
#
# 3. Pour vérifier vos résultats, ouvrez la base en parallèle :
#    uv run sqlite3 lab.db
#    puis SELECT * FROM formes;


# ============================================================================
# SCÉNARIO DE TEST FOURNI - Ne pas modifier.
# ============================================================================

if __name__ == "__main__":
    # Lecture (fournie) : devrait afficher les 6 formes de départ
    print("Formes dans la base :")
    for row in lister_formes():
        print(f"  #{row['forme_id']} {row['categorie']} dans le dessin {row['dessin_id']}")

    # TODO 1 : ajouter une forme
    nouveau = ajouter_forme(1, Cercle(Point(5.0, 5.0), 1.0))
    assert nouveau is not None, "ajouter_forme devrait retourner le forme_id"
    print(f"Cercle ajouté avec l'ID {nouveau}")

    # TODO 2 : relire la forme en objet
    forme = lire_forme(nouveau)
    assert isinstance(forme, Cercle), "lire_forme devrait reconstruire un Cercle"
    assert forme.centre.x == 5.0, "Le centre devrait être (5, 5)"

    # TODO 3 : déplacer
    assert deplacer_forme(nouveau, -1.0, 2.0), "deplacer_forme devrait retourner True"
    forme = lire_forme(nouveau)
    assert (forme.centre.x, forme.centre.y) == (4.0, 7.0), "Le centre devrait être (4, 7)"

    # TODO 4 : supprimer
    assert supprimer_forme(nouveau), "supprimer_forme devrait retourner True"
    assert lire_forme(nouveau) is None, "La forme ne devrait plus exister"
    assert not supprimer_forme(nouveau), "Supprimer deux fois devrait retourner False"

    print("Tous les tests ont réussi!")
