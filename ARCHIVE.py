import os
import shutil

def archive():
    # Définition des chemins relatifs
    source_folder = "hdfs/"
    destination_folder = "archive/"

    # S'assurer que le dossier de destination existe pour éviter les erreurs
    os.makedirs(destination_folder, exist_ok=True)

    # Lister tous les fichiers du dossier source
    files = os.listdir(source_folder)

    if not files:
        print("Aucun fichier à archiver dans le dossier hdfs/.")
        return

    for file_name in files:
        source_path = os.path.join(source_folder, file_name)
        
        # S'assurer qu'il s'agit bien d'un fichier (et non d'un sous-dossier)
        if os.path.isfile(source_path):
            destination_path = os.path.join(destination_folder, file_name)
            
            # Déplacement du fichier
            shutil.move(source_path, destination_path)
            print(f"Fichier déplacé : {file_name} -> archive/")

# Point d'entrée pour tester localement
if __name__ == "__main__":
    archive()