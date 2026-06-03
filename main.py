import os
import shutil
def collecte(chemin_fichier_externe):
    try:
        nom_fichier = os.path.basename(chemin_fichier_externe)
        fichier_destination = os.path.join("source", nom_fichier)
        shutil.copy(chemin_fichier_externe, fichier_destination)
        print(
            f"[COLLECTE] Succès : Le fichier '{nom_fichier}' a été extrait et copié dans 'source/'."
        )
    except Exception as e:
        print(f"[COLLECTE] Erreur lors de l'extraction : {e}")
if __name__ == "__main__":
    print("--- Test de la Collecte Dynamique ---")
    chemin_test = r"C:\Master1\ETL_Pharmacie\data\donnees_csv\Dim_Client.csv"
    collecte(chemin_test)