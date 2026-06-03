
import shutil, os

def load_hdfs():

    source_file = "source/"
    destination_file = "hdfs/"

    for file in os.listdir(source_file):
        source = os.path.join(source_file, file)
        destination = os.path.join(destination_file, file)
        shutil.move(source, destination)
        print(f"{file} a été déplacé dans hdfs/")

if __name__ == "__main__":
    
    load_hdfs()