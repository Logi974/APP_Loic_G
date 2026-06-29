-- Données d'exemple du laboratoire - VERSION ÉTUDIANT

-- ============================================================================
-- Dessins
-- ============================================================================

INSERT INTO dessins (dessin_id, titre) VALUES
    (1, 'Maison'),
    (2, 'Bonhomme de neige');

-- ============================================================================
-- Formes
-- ============================================================================

INSERT INTO formes (forme_id, dessin_id, categorie, centre_x, centre_y,
                    largeur, hauteur, rayon) VALUES
    (1, 1, 'rectangle', 0.0,  0.0,  8.0, 5.0, NULL),  -- les murs
    (2, 1, 'carre',    -2.0,  1.0,  2.0, 2.0, NULL),  -- la fenêtre
    (3, 1, 'rectangle', 2.0, -1.5,  1.5, 2.0, NULL),  -- la porte
    (4, 2, 'cercle',    0.0, -2.0, NULL, NULL, 2.0),  -- la base
    (5, 2, 'cercle',    0.0,  1.0, NULL, NULL, 1.5),  -- le tronc
    (6, 2, 'cercle',    0.0,  3.5, NULL, NULL, 1.0);  -- la tête
