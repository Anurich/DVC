from sentence_transformers import SentenceTransformer
from config import CONFIG
import pandas as pd
import faiss
import os
from tqdm import tqdm 
from pprint import pprint
import numpy as np
import faiss

class findEmbedding:
    def __init__(self) -> None:
        self.df = pd.read_csv(CONFIG.REFRACTOR_FILE_PATH)
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        embeddings = self.computeEmbeddings()
        # let's check if the folder exist 
        if not os.path.isdir(CONFIG.SAVE_EMBEDDINGS):
            os.mkdir(CONFIG.SAVE_EMBEDDINGS)
        #save the embedding file.
        PATH = os.path.join(CONFIG.SAVE_EMBEDDINGS, "embedding.npy")
        with open( PATH, "wb") as fp:
            np.save(fp, embeddings)

    def computeEmbeddings(self):
        sentences = self.df["prepText"].values
        # let's compute the embeddding
        embeddings = []
        for sentence in tqdm(sentences):
            embeddings.append(self.model.encode(sentence))

        return np.array(embeddings)


class recmmSystem:
    def __init__(self) -> None:
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.df = pd.read_csv(CONFIG.REFRACTOR_FILE_PATH)
        PATH = os.path.join(CONFIG.SAVE_EMBEDDINGS, "embedding.npy")
        embeddings = np.load(PATH)
        dimension = embeddings.shape[1]
        quantize = faiss.IndexFlatL2(dimension)
        self.index = faiss.IndexIVFFlat(quantize, dimension, 50)

        if not self.index.is_trained:
            self.index.train(embeddings)
        
        if self.index.is_trained:
            # let's add this 
            self.index.add(embeddings)

        print("Total Number of embeddings index {}".format(self.index.ntotal))
    
    def nearestNeighbour(self, query, k):
        # we can now search 
        queryEmbeddings = self.model.encode([query])
        D, I = self.index.search(queryEmbeddings, k)
        # let's get the index result 
        artist_songs = dict()
        allRelatable = self.df.iloc[I[0]]
        for index, rows in allRelatable.iterrows():
            artist_songs[rows["artist"]] = rows["song"]
        
        print("Query: ", query)
        pprint(artist_songs)



if __name__ =="__main__":   
    if not os.path.isdir(CONFIG.SAVE_EMBEDDINGS):
        findEmbedding()

    rcSystem = recmmSystem()
    rcSystem.nearestNeighbour("rock song heavy metal", 5)