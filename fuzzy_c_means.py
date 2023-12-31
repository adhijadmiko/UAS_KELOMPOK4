# -*- coding: utf-8 -*-
"""fuzzy_c_means.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zZuMX-zqGASqEPDzBQEJCUwOmKDlK139
"""

#import library yang diperlukan
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

data_pengangguran= pd.read_excel('/dataset.xlsx')

print(data_pengangguran.head())

K = 3
m = 3

U=np.random.rand(data_pengangguran.shape[0],K)
U/=np.sum(U, axis =1)[:,np.newaxis]
U

def calculate_centroid (data_pengangguran, K, U, m):
  Centroids=np.zeros((K, data_pengangguran.shape[1]))
  for i in range (K):
    Centroids[i,:]=np.sum((U[:,i]**m)[:,np.newaxis]*data_pengangguran, axis=0)/np.sum(U[:,i]**m)
    return Centroids

def calculate_membership (data_pengangguran, Centroids, K, m):
  U_new=np.zeros((data_pengangguran.shape[0],K))
  for i in range (K):
    U_new[:,i]=np.linalg.norm(data_pengangguran-Centroids[i,:],axis=1)

  U_new=1/ (U_new**(2/(m-1))*np.sum((1/U_new) ** (2/(m-1)),  axis=1 )[:,np.newaxis])
  return U_new

labels = np.argmax(U_new, axis=1)
labels

#first plot
sns.scatterplot(data_pengangguran=data_pengangguran, x=data_pengangguran[:,0],y=data_pengangguran[:,1], hue=labels, pallete='nipy_spectral')

max_iteration=100
for iteration in range (max_iteration):
  Centroids=calculate_centroid(data_pengangguran, 3, U, 3)
  U_new= calculate_membership (data_pengangguran, Centroids, 3, 3)

  if np.linalg.norm (U_new- U) <=0.0001:
    break
  U=U_new
    labels=np.argmax(U_new, axis=1)

#second plot
sns.scatterploy(data_pengangguran=data_pengangguran, x=data_pengangguran[:,0], y=data_pengangguran[:,1], huee=labels, pallete = 'nipy_spectral')
