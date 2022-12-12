import pandas as pd
import string
import re 
from config import CONFIG

class PREPROCESS:
    def __init__(self) -> None:
        df = pd.read_csv(CONFIG.DATA_FILE)
        df["prepText"] = df["text"].apply(self.cleanString)
        df = df[["artist", "song", "prepText"]]
        df["allText"] = df["artist"]+" "+df["song"] + " "+df["prepText"]
        # save the file 
        df.to_csv(CONFIG.REFRACTOR_FILE_PATH, index=False)
    
    def cleanString(self,sentence):
        sentence = sentence.translate(str.maketrans("","", string.punctuation)).strip().lower()
        sentence = re.sub(r"https?://\s+", "", sentence)
        sentence = re.sub(r"\b\d+\b",  "", sentence)
        sentence = re.sub(r" +"," ",sentence).replace("\n", " ").replace("\r", "").replace("\r\n", "")
        sentence = re.sub("\s+", " ", sentence)
        return sentence    



PREPROCESS()
