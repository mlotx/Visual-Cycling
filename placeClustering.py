import json
from pprint import pprint
import sys
from datetime import datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.stats import mode
import operator
from matplotlib import dates as md

import glob





import numpy as np
import pylab as pl

from sklearn.cluster import MiniBatchKMeans, KMeans
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.datasets.samples_generator import make_blobs


class Places():
    def __init__(self):
       self.allPlaceNumChanges = []
       self.firstPlaceNumChanges = []
       self.secondPlaceNumChanges = []
       self.thirdPlaceNumChanges = []
        
                
    def readFile(self,filename,race = "", gender = "", year = "", location="", racetype= ""):
        if race in filename and gender in filename and year in filename and location in filename and racetype in filename:
            print filename
            json_data=open(filename,'r')
            data = json.load(json_data)
            self.getPlace(data)

    def getPlace(self,data):
        
        for rider in data:
            startPosition = -1
            numberChanges = -1
            pastPostition = -1
            for lap in rider['Laps']:
                if 'place' in lap:
                    if lap['place'] != -1:
                        if startPosition == -1:
                            startPosition = lap['place'] 
                        if lap['place'] != pastPostition:
                            pastPostition = lap['place']
                            numberChanges +=1
                else:
                    break
            
            if numberChanges != -1:
                self.allPlaceNumChanges.append([int(pastPostition), int(numberChanges)])
                if pastPostition == 1:
                    self.firstPlaceNumChanges.append([int(startPosition), int(numberChanges)])
                if pastPostition == 2:
                    self.secondPlaceNumChanges.append([int(startPosition), int(numberChanges)])
                if pastPostition == 3:
                    self.thirdPlaceNumChanges.append([int(startPosition), int(numberChanges)])
            
def clustering(data, name):
    n_clusters = 4
    k_means = KMeans(n_clusters = 4, n_init = 10)
    k_means.fit(data)
    k_means_cluster_centers = k_means.cluster_centers_
    k_means_labels = k_means.labels_

    
    pl.figure()
    colors = ['#4EACC5', '#FF9C34', '#4E9A06','#FFFF33']
  
    x_data = []
    y_data = []
    for point in data:
        x_data.append(point[0])
        y_data.append(point[1])

    cluster = 0
    for k, col in zip(range(n_clusters), colors):
        my_members = k_means_labels == k
        cluster_center = k_means_cluster_centers[k]
        for p in range (0, len(k_means_labels)-1):
            if k_means_labels[p] == cluster:
                pl.plot(x_data[p], y_data[p],  'o',  markerfacecolor = col, markeredgecolor='k', markersize=5)
        cluster +=1
        
        pl.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
                markeredgecolor='k', markersize=10)

  
    pl.title(name)
    pl.show()
   
                



def main():
    st = Places()

   
    inputRace = "Team"
    inputGender = ""
    inputYear = ""
    inputLocation = ""
    inputRacetype ="Qualifying"


   
    for filename in sys.argv[1:]:
        st.readFile(filename, race = inputRace,  year = inputYear, location = inputLocation, gender = inputGender,racetype =inputRacetype)

    clustering(st.allPlaceNumChanges,'Racer Place vs Number of Place Changes' )
    clustering(st.firstPlaceNumChanges, 'First Place: Starting Place vs Number of Place Changes')
    clustering(st.secondPlaceNumChanges, 'Second Place: Starting Place vs Number of Place Changes')
    clustering(st.thirdPlaceNumChanges, 'Third Place: Starting Place vs Number of Place Changes')

    

    



if __name__=="__main__":
    main()
