"""
Module models - Classes représentant les entités du système de gestion.
"""

from .bon_travail import BonTravail
from .client import Client
from .robot import Robot

__all__ = [
    "Client",
    "Robot",
    "BonTravail",
]
