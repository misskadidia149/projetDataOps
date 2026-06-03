import os
import shutil


def collecte(chemin_fichier_externe):
    try:
        shutil.copy(chemin_fichier_externe, os.path.join("source", "data.csv"))
        print("[COLLECTE] Succès : Fichier copié avec succès.")
    except Exception as e:
        print(f"[COLLECTE] Erreur : {e}")


if __name__ == "__main__":
    chemin_test = r"C:\Master1\ETL_Pharmacie\data\donnees_csv\Dim_Produit.csv"
    collecte(chemin_test)