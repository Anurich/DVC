# Music Recommendation System Using Sentence Transformers, Faiss with DVC.
## Task
This repository show the very basic music recommendation system. For this task we have used DVC to store the heavy data into the remote location while keep the code files in github repository. In this task I have used Sentence Transformers for computing Embeddings, and faiss for searching process.
## DVC
DVC is a framework of MLOps, It give us many functionalities like:
  * Experiment Tracking.
  * Data, Model, Code Versioning.
  * Code Reproducibility.
  
In this experimentation I focused on:
  * Model, data, code versioning.
  * code reproducibility.
## How DVC is used.
<pre>
  <code>
    # initialise the DVC 
    dvc init
    
    
    # set the credential for the remote location 
    dvc remote add origin **enter your repository**
    dvc remote modify origin --local auth **basic**
    dvc remote modify origin --local user **username**
    dvc remote modify origin --local **password your_token**

    # now we can run the particular file for which we wanted our output to be tracked by DVC 
    dvc run -n dataPreprocessing -d filepath -o outputpath python3 filename.py
    
    # than we can add the three file inside the git which tells git to ignore the output of this file
    git add dvc.lock dvc.yaml .gitignore
    # we can also do 
    git add .

    # next is to commit the changes 
    Git commit -m “v1.1”
    Git tag “v1.1”

    # now we push
    Git push -u origin main 
    Dvc push -r origin 

    # Roll back to different version is easy 
    git checkout v1.1
    dvc pull
    
  </code>
</pre>


## Dataset Information.
The dataset used is  <b> Spotify Million Song Dataset </b> taken from kaggle which can be downloaded from link <a href="https://www.kaggle.com/code/notshrirang/music-recommender-using-pair-similarities/data"> Download </a>


## Library Used 
* faiss
* pandas
* numpy
* sentence-transformers
* DVC

## Note.

Experiment in this repository is to show how we can use DVC for data, code, versioning, purpose of this repository is not have the perfect recommendation system.
