#Tache 1 : collecter les données à partir d'un fichier externe et les copier dans le dossier source/
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


#






# Tâche 3: Créer la fonction tl_hive() pour copier ou charger le fichier du dossier hdfs/ vers le dossier hive/
import shutil, os
def tl_hive():
    source_dir = 'hdfs/'
    destination_dir = 'hive/'

    for file in os.listdir(source_dir):
        source= os.path.join(source_dir, file)
        destination=os.path.join(destination_dir,file)
        shutil.copy(source, destination)
# Appeler la fonction tl_hive() pour exécuter la tâche



if __name__ == "__main__":
    print("--- Test de la Collecte Dynamique ---")
    chemin_test = r"C:\Master1\ETL_Pharmacie\data\donnees_csv\Dim_Client.csv"
    collecte(chemin_test)
    tl_hive()

