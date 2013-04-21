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


class RaceStats():
    def __init__(self):
        self.LapTimeDict ={}
        self.racerDict = {}
                
    def readFile(self,filename,race = "", gender = "", year = "", location="", racetype= ""):
        if race in filename and gender in filename and year in filename and location in filename and racetype in filename:
            print filename
            json_data=open(filename,'r')
            data = json.load(json_data)
            self.getLapTimes(data)

    def getLapTimes(self,data):
        for rider in data:
            place = -1
            laps = rider['Laps']
            pastTime = datetime.strptime('00:00:00.000000','%H:%M:%S.%f') 
            tempList = []
            for lap in laps:
                if lap['place'] > 0:
                    temptime = self.timeStrToTime(lap['time'])
                    time = temptime - pastTime
                    if len(str(time)) ==7:
                        convertingtime = datetime.strptime(str (time)+'.000000','%H:%M:%S.%f')
                    else:
                        convertingtime = datetime.strptime(str (time),'%H:%M:%S.%f')
                    tempList.append(convertingtime)
                    pastTime = temptime
                    place = lap['place']
            self.LapTimeDict[place] = tempList
            if rider['Team']:
                self.racerDict[place] = rider['Team']
        

    def timeStrToTime(self,string):
        if len(string) == 8:
            timeObject= datetime.strptime(string,'%H:%M:%S')
        else:
            timeObject= datetime.strptime(string,'%H:%M:%S.%f')

        return timeObject
                    

                



def main():
    st = RaceStats()
    
    inputRace = "TeamPursuit"
    inputGender = "Men"
    inputYear = "2011"
    inputLocation = "Cali"
    inputRacetype ="Final"


  
    for filename in sys.argv[1:]:
        st.readFile(filename, race = inputRace,  year = inputYear, location = inputLocation, gender = inputGender,racetype =inputRacetype)

    labels = []
    plotingPlots = []
    
    for rider in st.LapTimeDict:
        tempPlace = rider
        testing = st.LapTimeDict[rider]
        newdates = []
        labels.append(str(tempPlace))
        
        
        for item in testing:
            newdates = [md.date2num(item) for item in testing]
            p, = plt.plot(newdates)
            plotingPlots.append(p)
        

    plt.legend(plotingPlots, labels, loc = 9, ncol= 5)
    plt.ylabel('time')
    plt.show()

    



if __name__=="__main__":
    main()
