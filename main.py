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