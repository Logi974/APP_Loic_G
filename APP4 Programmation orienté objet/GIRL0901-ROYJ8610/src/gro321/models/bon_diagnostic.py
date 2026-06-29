from ..models import BonTravail, Piece

class BonDiagnostic(BonTravail):
    """
    Classe dérivée représentant un bon de travail de diagnostic.
    """

    def __init__(self, bon_id, numero_serie, date_creation=None, statut="ouvert", symptomes=None, diagnostic=None, pieces:list[Piece]=[]):
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
        super().__init__(bon_id, numero_serie, date_creation, statut, "diagnostic", pieces)

        self.symptomes = symptomes
        self.diagnostic = diagnostic

    def obtenir_description(self):
        """
        Retourne une description du bon de diagnostic.
        """
        
        desc = "Bon de travail de type diagnostic.\n"
        desc += f"Symptomes : {self.symptomes if self.symptomes != None else 'Aucun'},\n"
        desc += f"Diagnostic : {self.diagnostic if self.diagnostic != None else 'Aucun'}"

        return desc
