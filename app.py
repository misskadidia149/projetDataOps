import os
import random

def charger_donnees(chemin_fichier):
    """Vérifie la présence du fichier et simule son chargement."""
    if not os.path.exists(chemin_fichier):
        print(f"Erreur : Le fichier '{chemin_fichier}' n'existe pas.")
        return False
    
    print(f"Succès : Fichier '{chemin_fichier}' trouvé et chargé avec succès !")
    return True


def generer_mdp(n):
    caractere=("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    mot_de_passe= ""
    for i in range(n):
        mot_de_passe +=random.choice(caractere)
    return mot_de_passe
print(generer_mdp(12))
print(generer_mdp(5))

if __name__ == "__main__":
    # Test de la fonction
    charger_donnees("mon_fichier.csv")


