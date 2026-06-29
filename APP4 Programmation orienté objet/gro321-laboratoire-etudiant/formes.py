"""
Module des formes géométriques - VERSION ÉTUDIANT.

EXERCICE 1 du laboratoire :
Implémenter la hiérarchie de classes vue à l'activité procédurale 1 :
une classe parente Forme et les classes dérivées Rectangle, Cercle,
Carré (qui dérive de Rectangle) et Polygone (défi).

La classe Point est FOURNIE comme exemple : étudiez-la avant de commencer.
Exécutez ce fichier pour lancer les tests : python formes.py
(dans l'environnement du cours : uv run python formes.py)
"""

import math


class Point:
    """
    Un point du plan.

    CLASSE FOURNIE comme exemple. Remarquez :
    - le constructeur __init__ qui initialise les attributs;
    - l'argument self, qui fait référence à l'instance;
    - la méthode __repr__, appelée pour afficher l'objet.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


class Forme:
    """
    Classe parente de toutes les formes fermées.

    Chaque forme a un centre (un Point). Le calcul d'aire dépend de la
    catégorie de forme : la méthode aire() est donc redéfinie dans chaque
    classe dérivée. Ici, elle lève une exception si la classe dérivée a
    oublié de la redéfinir. (On verra à la prochaine activité procédurale une façon
    plus formelle de déclarer ce genre de contrat : les classes abstraites.)
    """

    def __init__(self, centre : Point):
        self.centre = centre

    def aire(self):
        raise NotImplementedError("aire() doit être redéfinie par la classe dérivée")

    def deplacer(self, dx, dy):
        """
        Déplace la forme de dx en x et de dy en y.

        """
        self.centre.x += dx
        self.centre.y += dy


class Rectangle(Forme):
    """
    Un rectangle aligné sur les axes, défini par son centre,
    sa largeur et sa hauteur.

    TODO: À IMPLÉMENTER

    Instructions :
    1. Écrire le constructeur __init__(self, centre, largeur, hauteur) :
       - appeler le constructeur du parent avec super().__init__(centre);
       - initialiser les attributs largeur et hauteur.
    2. Redéfinir aire() : largeur × hauteur.
    """

    # TODO: Implémenter le constructeur et aire()
    
    def __init__(self, centre : Point, largeur : float, hauteur : float):
        super().__init__(centre)
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur


class Cercle(Forme):
    """
    Un cercle défini par son centre et son rayon.

    TODO: À IMPLÉMENTER

    Instructions :
    1. Écrire le constructeur __init__(self, centre, rayon).
    2. Redéfinir aire() : π × rayon² (utilisez math.pi).
    """

    # TODO: Implémenter le constructeur et aire()
    def __init__(self, centre : Point, rayon : float):
        super().__init__(centre)
        self.rayon = rayon

    def aire(self):
        return math.pi*(self.rayon**2)


class Carre(Rectangle):
    """
    Un carré : un rectangle dont la largeur et la hauteur sont égales.

    TODO: À IMPLÉMENTER

    Instructions :
    1. Écrire le constructeur __init__(self, centre, taille) qui appelle
       le constructeur de Rectangle avec la même valeur pour la largeur
       et la hauteur.
    2. C'est tout ! aire() et deplacer() sont héritées. Posez-vous la
       question : d'où vient chacune des deux ?
    """

    # TODO: Implémenter le constructeur
    def __init__(self, centre : Point, taille : float):
        super().__init__(centre, taille, taille)


class Polygone(Forme):
    """
    Un polygone arbitraire défini par une liste de Points (ses sommets).

    TODO 5 (DÉFI, optionnel) : À IMPLÉMENTER

    Instructions :
    1. Écrire le constructeur __init__(self, centre, points) où points
       est une liste d'au moins 3 Points.
    2. Redéfinir aire() avec la formule du lacet (shoelace) :
       aire = (1/2) * | somme de (x_i * y_(i+1) - x_(i+1) * y_i) |
       où le sommet suivant le dernier est le premier (indices modulo n).
    3. Redéfinir deplacer(dx, dy) pour déplacer le centre ET tous les
       sommets. Pensez à réutiliser la méthode du parent avec super().
    """

    # TODO (défi): Implémenter le constructeur, aire() et deplacer()
    
    def __init__(self, centre : Point, points : list):
        super().__init__(centre)
        if len(points) < 3:
            raise ValueError("Un polygone doit avoir au moins 3 sommets.")
        self.points = points

    def aire(self):
        n = len(self.points)
        area = 0.0
        for i in range(n):
            j = (i + 1) % n  # sommet suivant, avec wrap-around
            area += self.points[i].x * self.points[j].y
            area -= self.points[j].x * self.points[i].y
        return abs(area) / 2.0

    def deplacer(self, dx : float, dy : float):
        super().deplacer(dx, dy)  # Déplace le centre
        for point in self.points:
            point.x += dx
            point.y += dy


# ============================================================================
# TESTS FOURNIS - Ne pas modifier.
# Tous les tests doivent réussir une fois les TODO 1 à 4 complétés.
# Les tests du TODO 5 (Polygone) sont désactivés par défaut.
# ============================================================================

if __name__ == "__main__":
    # TODO 1 : Rectangle
    r = Rectangle(Point(0.0, 0.0), 4.0, 2.0)
    assert r.aire() == 8.0, "L'aire du rectangle 4x2 devrait être 8"

    # TODO 2 : deplacer (héritée de Forme)
    r.deplacer(1.0, -2.0)
    assert (r.centre.x, r.centre.y) == (1.0, -2.0), "Le centre devrait être (1, -2)"

    # TODO 3 : Cercle
    c = Cercle(Point(1.0, 1.0), 2.0)
    assert abs(c.aire() - 4.0 * math.pi) < 1e-9, "L'aire du cercle de rayon 2 devrait être 4π"

    # TODO 4 : Carré
    k = Carre(Point(0.0, 0.0), 3.0)
    assert k.aire() == 9.0, "L'aire du carré de taille 3 devrait être 9"
    assert isinstance(k, Rectangle), "Un carré devrait être un Rectangle"
    assert isinstance(k, Forme), "Un carré devrait être une Forme"

    # TODO 5 (défi) : retirez le commentaire pour tester Polygone
    p = Polygone(Point(0.0, 0.0), [Point(0.0, 0.0), Point(4.0, 0.0), Point(0.0, 3.0)])
    assert abs(p.aire() - 6.0) < 1e-9, "L'aire du triangle devrait être 6"
    p.deplacer(1.0, 1.0)
    assert (p.points[0].x, p.points[0].y) == (1.0, 1.0), "Les sommets doivent suivre"

    print("Tous les tests ont réussi!")
