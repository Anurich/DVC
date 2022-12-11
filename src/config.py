import os 
class CONFIG:
    PATH = os.getcwd()
    REFRACTOR_FILE_PATH = os.path.join(PATH, "dataset/refactor.csv")
    DATA_FILE = os.path.join(PATH, "dataset/spotify_millsongdata.csv")