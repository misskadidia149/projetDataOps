import os

def charger_donnees(chemin_fichier):
    """Vérifie la présence du fichier et simule son chargement."""
    if not os.path.exists(chemin_fichier):
        print(f"Erreur : Le fichier '{chemin_fichier}' n'existe pas.")
        return False
    
    print(f"Succès : Fichier '{chemin_fichier}' trouvé et chargé avec succès !")
    return True

if __name__ == "__main__":
    # Test de la fonction
    charger_donnees("mon_fichier.csv")