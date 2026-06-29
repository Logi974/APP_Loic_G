-- Données d'exemple pour la base de départ
--
-- Les clients et les robots sont normalisés: chaque client n'apparait qu'une
-- seule fois et chaque robot reference son client par client_id.

-- ============================================================================
-- CLIENTS ET ROBOTS (CODE DE RÉFÉRENCE NORMALISÉ)
-- ============================================================================

-- Insertion des clients (une seule fois chacun)
INSERT INTO clients (client_id, nom, contact, adresse) VALUES
    (1, 'Restaurant Le Gourmet', '514-555-1234', '123 rue Principale, Montréal'),
    (2, 'Hôtel Plaza', '418-555-5678', '456 boulevard Royal, Québec'),
    (3, 'Café Central', '450-555-9012', '789 avenue Centrale, Laval');

-- Insertion des robots avec référence au client
INSERT INTO robots (robot_id, modele, numero_serie, statut, client_id) VALUES
    (1, 'ServBot-2000', 'SN-2024-001', 'operationnel', 1),
    (2, 'ServBot-2000', 'SN-2024-002', 'operationnel', 1),
    (3, 'ServBot-3000', 'SN-2024-003', 'en_maintenance', 1),
    (4, 'ServBot-2000', 'SN-2024-004', 'operationnel', 2),
    (5, 'ServBot-3000', 'SN-2024-005', 'operationnel', 2),
    (6, 'ServBot-2000', 'SN-2024-006', 'hors_service', 3);

-- ============================================================================
-- BONS DE TRAVAIL (PREUVE DE CONCEPT, NON NORMALISÉ)
-- ============================================================================
-- Le robot est désigné par son numéro de série (pas de clé étrangère).
-- Beaucoup de colonnes sont NULL selon le type de bon.

-- Tous les bons de travail
INSERT INTO bons_travail (bon_id, robot_id, type_bon, date_creation, statut) VALUES
    (1, 3, 'diagnostic', '2024-06-01 10:30:00', 'termine'),
    (2, 1, 'mise_a_jour', '2024-06-05 14:00:00', 'termine'),
    (3, 2, 'mise_a_jour', '2024-06-05 14:30:00', 'en_cours'),
    (4, 6, 'reparation', '2024-06-03 09:00:00', 'termine'),
    (5, 4, 'diagnostic', '2024-06-08 11:00:00', 'ouvert'),
    (6, 5, 'reparation', '2024-06-07 16:00:00', 'en_cours');

-- Infos sur les bons de diagnostic
INSERT INTO diagnostic (diagnostic_id, bon_id, symptomes, diagnostic) VALUES
    (1, 1, 'Le robot tourne en rond et ne suit pas les trajectoires', 'Capteur LIDAR avant défectueux'),
    (2, 5, 'Bruit anormal lors des virages', NULL);

-- Infos sur les bons de mise à jour
INSERT INTO mise_a_jour (maj_id, bon_id, version_actuelle, version_cible, mise_a_jour_reussie) VALUES
    (1, 2, 'v1.2.3', 'v2.0.0', 1),
    (2, 3, 'v1.2.3', 'v2.0.0', NULL);

-- Infos sur les bons de réparation
INSERT INTO reparation (reparation_id, bon_id, composant, probleme) VALUES
    (1, 4, 'Moteur roue gauche', 'Moteur ne répond plus aux commandes'),
    (2, 6, 'Batterie', 'Autonomie réduite de 50%');

-- Pièces disponibles
INSERT INTO piece (piece_id, nom) VALUES
    (1, 'Moteur NEMA-17'),
    (2, 'Courroie');

-- Pièces nécessaires pour les différents bons de travail
INSERT INTO liste_piece (bon_id, piece_id, quantite) VALUES
    (4, 1, 1),
    (4, 2, 1);
