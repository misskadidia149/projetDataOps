import os

def collecte():
    """
    Étape1 :python main.py Collecte
    Vérifie la présence du fichier de données dans le dossier source.
    """
    # os.path.join s'assure que le chemin fonctionne sur Windows et Linux
    chemin_source = os.path.join("source", "data.csv")
    
    if os.path.exists(chemin_source):
        print(f"[COLLECTE] Succès : Le fichier {chemin_source} a été détecté.")
        return True
    else:
        print(f"[COLLECTE] Échec : Le fichier {chemin_source} est introuvable.")
        return False

if __name__ == "__main__":
    print("--- Test local de la Collecte ---")
    collecte()