-- Schéma de base de données du laboratoire - VERSION ÉTUDIANT
-- Un dessin vectoriel contient des formes (voir l'activité procédurale 1).

-- ============================================================================
-- Table des dessins
-- ============================================================================

CREATE TABLE IF NOT EXISTS dessins (
    dessin_id INTEGER PRIMARY KEY AUTOINCREMENT,
    titre     TEXT NOT NULL
);

-- ============================================================================
-- Table des formes
-- ============================================================================

-- NOTE: les colonnes largeur, hauteur et rayon ne s'appliquent pas à toutes
-- les catégories (beaucoup de NULL!). Gardez cette observation en tête :
-- on verra à la prochaine activité procédurale pourquoi c'est le signe
-- d'une conception à revoir.

CREATE TABLE IF NOT EXISTS formes (
    forme_id  INTEGER PRIMARY KEY AUTOINCREMENT,
    dessin_id INTEGER NOT NULL,
    categorie TEXT NOT NULL,
    centre_x  REAL NOT NULL,
    centre_y  REAL NOT NULL,

    largeur   REAL,   -- rectangle et carré
    hauteur   REAL,   -- rectangle et carré
    rayon     REAL,   -- cercle

    FOREIGN KEY (dessin_id) REFERENCES dessins(dessin_id),
    CHECK (categorie IN ('rectangle', 'carre', 'cercle'))
);
