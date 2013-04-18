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
    print 'Number of Races:', len(sys.argv), 'files'
   
    inputRace = "TeamPursuit"
    inputGender = "Mens"
    inputYear = "2011"
    inputLocation = "Cali"
    inputRacetype ="Qualifying"


  
    for filename in sys.argv[1:]:
        st.readFile(filename, race = inputRace,  year = inputYear, location = inputLocation, gender = inputGender,racetype =inputRacetype)


    for rider in st.LapTimeDict:
        testing = st.LapTimeDict[rider]

        newdates = []
        for item in testing:
            newdates = [md.date2num(item) for item in testing]

        
        
        plt.plot(newdates)
    
    plt.ylabel('time')
    plt.show()

    



if __name__=="__main__":
    main()
