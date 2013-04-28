import copy
import csv
import json
import math
import sys
import pprint
from datetime import datetime, timedelta

class SplitTime():
    def __init__(self):
        self.MensTeamPursuitStart = []
        self.MensTeamPursuit = []
        self.WomensTeamPursuitStart = []
        self.WomensTeamPursuit = []
        self.MensIndividualPursuitStart = []
        self.MensIndividualPursuit = []
        self.WomensIndividualPursuitStart = []
        self.WomensIndividualPursuit = []
        self.MensTeamSprintStart = []
        self.MensTeamSprint = []
        self.WomensTeamSprintStart = []
        self.WomensTeamSprint = []
        self.MensKiloStart = []
        self.MensKilo = []

    def finish(self):
        jsonFile = open('lapTimes.json','w')
        JsonToDump = {}
        JsonToDump['MensTeamPursuitStart']=self.MensTeamPursuitStart
        JsonToDump['MensTeamPursuit']=self.MensTeamPursuit
        JsonToDump['WomensTeamPursuitStart']=self.WomensTeamPursuitStart
        JsonToDump['WomensTeamPursuit']=self.WomensTeamPursuit
        JsonToDump['MensIndividualPursuitStart']=self.MensIndividualPursuitStart
        JsonToDump['MensIndividualPursuit']=self.MensIndividualPursuit
        JsonToDump['WomensIndividualPursuitStart']=self.WomensIndividualPursuitStart
        JsonToDump['WomensIndividualPursuit']=self.WomensIndividualPursuit
        JsonToDump['MensTeamSprintStart']=self.MensTeamSprintStart
        JsonToDump['MensTeamSprint']=self.MensTeamSprint
        JsonToDump['WomensTeamSprintStart']=self.WomensTeamSprintStart
        JsonToDump['WomensTeamSprint']=self.WomensTeamSprint
        JsonToDump['MensKiloStart'] = self.MensKiloStart
        JsonToDump['MensKilo'] = self.MensKilo
        json.dump(JsonToDump,jsonFile)
        jsonFile.close()
                
    def readFile(self,filename):
        json_data=open(filename,'r')
        data = json.load(json_data)
        if filename.find('MensTeamPursuit')>0:
            self.addTimes(data,self.MensTeamPursuitStart,self.MensTeamPursuit)
        elif filename.find('WomensTeamPursuit')>0:
            self.addTimes(data,self.WomensTeamPursuitStart,self.WomensTeamPursuit)
        elif filename.find('MensIndividualPursuit')>0:
            self.addTimes(data,self.MensIndividualPursuitStart,self.MensIndividualPursuit)
        elif filename.find('WomensIndividualPursuit')>0:
            self.addTimes(data,self.WomensIndividualPursuitStart,self.WomensIndividualPursuit)
        elif filename.find('MensTeamSprint')>0:
            self.addTimes(data,self.MensTeamSprintStart,self.MensTeamSprint)
        elif filename.find('WomensTeamSprint')>0:
            self.addTimes(data,self.WomensTeamSprintStart,self.WomensTeamSprint)
        elif filename.find('MensKilo')>0:
            self.addTimes(data,self.MensKiloStart,self.MensKilo)

        
    def addTimes(self,data,start,flying):
        for rider in data:
            perviousTime = datetime.strptime('00:00:00.000000','%H:%M:%S.%f')        
            for lap in rider['Laps']:
                lapTime = self.timeStrToTime(lap['time'])
                if lap['splitDistance']==250:
                    deltaTime = lapTime - perviousTime
                    start.append(float(str(deltaTime.seconds)+'.'+str(deltaTime.microseconds)))
                    perviousTime = lapTime
                elif lap['splitDistance']%250==0:
                    deltaTime = lapTime - perviousTime
                    flying.append(float(str(deltaTime.seconds)+'.'+str(deltaTime.microseconds)))
                    perviousTime = lapTime

    def timeStrToTime(self,string):
        if len(string) == 8:
            timeObject= datetime.strptime(string,'%H:%M:%S')
        else:
            timeObject= datetime.strptime(string,'%H:%M:%S.%f')

        return timeObject


class SplitTimeCSV():
    def __init__(self):
        jsonFile = open('lapTimes.json','r')
        data = json.load(jsonFile)
        countList = {}
        races = []
        for x in data:
            races.append(x)
            countList[x]=0
        splitLapCountDict = {}
        #12.477
        #25.867
        x=12.25
        while x<26:
            splitLapCountDict[x]=copy.deepcopy(countList)
            x+=.25
        for raceType in data:
            print raceType
            for split in data[raceType]:
                floorSplit = math.floor(split)
                if split<floorSplit+.25:
                    splitLapCountDict[floorSplit][raceType]+=1
                elif split<floorSplit+.5:
                    splitLapCountDict[floorSplit+.25][raceType]+=1
                elif split<floorSplit+.75:
                    splitLapCountDict[floorSplit+.5][raceType]+=1
                elif split<floorSplit+1:
                    splitLapCountDict[floorSplit+.75][raceType]+=1
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(splitLapCountDict)
        
        lapSplitCSV = open('csvs/lapSplit.csv','wb')
        lapSplitWriter = csv.writer(lapSplitCSV)
        lapSplitWriter.writerow(['Time']+races)
        for lapTime in sorted(splitLapCountDict.keys()):
            lapSplitWriter.writerow([lapTime]+splitLapCountDict[lapTime].values())

                

def main():
    st = SplitTime()
    print 'Number of Races:', len(sys.argv), 'files'
    for filename in sys.argv[1:]:
        #print filename
        st.readFile(filename)
    st.finish()

    SplitTimeCSV()


if __name__=="__main__":
    main()
