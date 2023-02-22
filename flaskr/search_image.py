import pickle
import numpy as np
import faiss
from flask import render_template, flash, render_template, request, redirect

def load_index():
    with open("./vectors/vectors_total.pkl","rb") as vector_file:
        vectors = pickle.load(vector_file)

    with open("./vectors/paths_total.pkl","rb") as path_file:
        paths = pickle.load(path_file)

    vector_dim = len(vectors[0])
    vectors = np.array(vectors)
    index = faiss.IndexFlatL2(vector_dim)
    index.add(vectors)

    return (index, vectors, paths)

def search(index, vector, all_paths, k):
    #k = 4
    k = int(request.form.get('quantity'))
    D, I = index.search(np.array([vector]), k)
    res_paths = np.array([])
    for i in I[0]:
        
        new_path = all_paths[i].replace('/content/drive/MyDrive/TruyvanDpt/test', '../static')
        res_paths = np.append(res_paths, new_path)
    return (D[0], res_paths)

