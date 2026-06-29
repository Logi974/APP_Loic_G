"""
Programme permettant de tester les différentes fonctions de crud_bons
"""

from src.gro321.database.crud_bons import *

def main():
    print("Tests des fonctions de CRUD\n")

    # Créer et lire un bon de diagnostic
    diag_id = creer_bon_diagnostic('SN-2024-001', 'Explosion spontanée')
    bon_diag = lire_bon(diag_id)
    print(bon_diag)
    print(f"Type : {bon_diag.__class__.__name__}")

    # Créer un bon de mise à jour
    maj_id = creer_bon_mise_a_jour('SN-2024-002', 'v1.0.0', 'v2.0.0')

    #Créer un bon de réparation
    creer_bon_reparation('SN-2024-003', 'Témoin lumineux', 'Aveuglement spontané')

    # Supprimer un bon
    supprimer_bon(bon_diag)

    # Modifier le statut d'un bon
    modifier_statut_bon(maj_id, 'termine')

    # Lister tous les bons
    print("Liste des bons")
    bons = lister_bons()
    print(bons, '\n')



if __name__ == "__main__":
    main()