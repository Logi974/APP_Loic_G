from ..models import BonTravail, Piece

class BonReparation(BonTravail):
    """
    Classe dérivée représentant un bon de travail de réparation.
    """

    def __init__(self, bon_id, numero_serie, date_creation=None, statut="ouvert", composant=None, probleme=None, pieces:list[Piece]=[]):
        """
        Initialise un bon de diagnostic.

        Args:
            bon_id: Identifiant unique du bon
            numero_serie: Numéro de série du robot concerné
            date_creation: Date de création (datetime ou None pour maintenant)
            statut: Statut du bon (ouvert, en_cours, termine, annule),
            symptomes : Problèmes notables sur le robot,
            diagnostic : Conclusion du diagnostic
        """
        super().__init__(bon_id, numero_serie, date_creation, statut, "reparation", pieces)

        self.composant = composant
        self.probleme = probleme

    def obtenir_description(self):
        """
        Retourne une description du bon de diagnostic.
        """
        
        desc = "Bon de travail de type réparation d'un robot.\n"
        desc += f"Composant : {self.composant if self.composant != None else 'Aucun'},\n"
        desc += f"Problème : {self.probleme if self.probleme != None else 'Aucun'}"

        return desc
