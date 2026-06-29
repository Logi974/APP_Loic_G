from ..models import BonTravail, Piece

class BonMiseAJour(BonTravail):
    """
    Classe dérivée représentant un bon de travail de mise à jour.
    """

    def __init__(self, bon_id, numero_serie, date_creation=None, statut="ouvert", version_actuelle=None, version_cible=None, pieces:list[Piece]=[]):
        """
        Initialise un bon de mise à jour.

        Args:
            bon_id: Identifiant unique du bon
            numero_serie: Numéro de série du robot concerné
            date_creation: Date de création (datetime ou None pour maintenant)
            statut: Statut du bon (ouvert, en_cours, termine, annule),
            version_actuelle : Version du logiciel à mettre à jour,
            version_cible : Nouvelle version du logiciel à mettre à jour
        """
        super().__init__(bon_id, numero_serie, date_creation, statut, "mise_a_jour", pieces)

        self.version_actuelle = version_actuelle
        self.version_cible = version_cible

    def obtenir_description(self):
        """
        Retourne une description du bon de diagnostic.
        """
        
        desc = "Bon de travail pour la mise à jour d'un robot.\n"

        va = self.version_actuelle
        vc = self.version_cible

        if va == None and vc == None:
            desc += "La version du logiciel reste à déterminer."
        elif va == None:
            desc += f"Le logiciel doit être mis à jour à la version {vc}"
        elif vc == None:
            desc += f"Le logiciel est présentement à la version {va} et doit être mis à jour à la version la plus récente."
        else:
            desc += f"Le logiciel doit être mis à jour de la version {va} à la version {vc}."

        return desc
