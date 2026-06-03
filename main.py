import os
import shutil

def collecte(chemin_fichier_externe):
    """
    Étape 1: Collecte 
    Prend un fichier externe (la source) et l'extrait (le copie) 
    dans le dossier 'source/' du projet sous le nom 'data.csv'.
    """
    # 1. Définir la destination obligatoire dans notre projet
    dossier_destination = "source"
    fichier_destination = os.path.join(dossier_destination, "data.csv")
    
    # 2. Vérifier si le fichier externe qu'on veut extraire existe vraiment
    if not os.path.exists(chemin_fichier_externe):
        print(f"[COLLECTE] Échec : Le fichier source externe '{chemin_fichier_externe}' est introuvable.")
        return False
        
    try:
        # 3. Créer le dossier 'source' s'il n'existe pas encore
        if not os.path.exists(dossier_destination):
            os.makedirs(dossier_destination)
            
        # 4. Extraire/Copier le fichier vers notre zone de stockage source
        shutil.copy(chemin_fichier_externe, fichier_destination)
        print(f"[COLLECTE] Succès : Fichier extrait de '{chemin_fichier_externe}' et copié vers '{fichier_destination}'.")
        return True
        
    except Exception as e:
        print(f"[COLLECTE] Erreur lors de l'extraction : {e}")
        return False

if __name__ == "__main__":
    print("--- Test de la Collecte Active ---")
    
    # Pour tester, remplace ce chemin par un vrai fichier qui existe sur ton PC !
    # Exemple : r"C:/Users/Dramane/Downloads/mon_nouveau_fichier.csv"
    chemin_test_externe = r"C:\Master1\ETL_Pharmacie\data\donnees_csv\Fait_Ventes.csv"
    
    collecte(chemin_test_externe)
# Tâche 3: Créer la fonction tl_hive() pour copier ou charger le fichier du dossier hdfs/ vers le dossier hive/
import shutil, os
def tl_hive():
    source_dir = 'hdfs/'
    destination_dir = 'hive/'

    for file in os.listdir(source_dir):
        source= os.path.join(source_dir, file)
        destination=os.path.join(destination_dir,file)
        shutil.move(source, destination)
# Appeler la fonction tl_hive() pour exécuter la tâche
tl_hive()