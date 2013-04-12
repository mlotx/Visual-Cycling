import json
from pprint import pprint
import sys
from datetime import datetime, timedelta


class SplitTime():
    def __init__(self):
        self.allTimes = []
        self.MensTimes = []
        self.WomensTimes = []
        self.teamTimes = []        
        self.individualTimes = []        
        self.individualPursuitTimes = []
        self.individualPursuitTimesMen = []
        self.individualPursuitTimesWomen = []
        self.teamPursuitTimes = []
        self.teamPursuitTimesMen = []
        self.teamPursuitTimesWomen = []
        self.teamSprint = []
        self.teamSprintMens = []
        self.teamSprintWomens = []
        self.startTimes = [] 
        self.startTimesMen = []
        self.startTimesWomen = []
        self.startTimesIP = [] 
        self.startTimesTP = [] 
        self.startTimesIPMens = []   
        self.startTimesIPWomens = []   
        self.startTimesTPMens = []   
        self.startTimesTPWomens = []
        self.startTimesTS = []
        self.startTimesTSMens = []   
        self.startTimesTSWomens = []   

                
    def readFile(self,filename):
        json_data=open(filename,'r')
        data = json.load(json_data)
        self.addTimes(data,self.allTimes)

        if filename.find('Men')>0:
            self.addTimes(data,self.MensTimes)
            self.addStartingLaps(data,self.startTimesMen)               
        else:
            self.addTimes(data,self.WomensTimes)
            self.addStartingLaps(data,self.startTimesWomen)
            


        if filename.find('Team')>0:
            self.addTimes(data,self.teamTimes)
        else:
            self.addTimes(data,self.individualTimes)


        if filename.find('IndividualPursuit')>0:
            self.addTimes(data,self.individualPursuitTimes)
            self.addStartingLaps(data,self.startTimesIP)
            if filename.find('Men')>0:
                self.addTimes(data,self.individualPursuitTimesMen)
                self.addStartingLaps(data,self.startTimesIPMens)
                
            else:
                self.addTimes(data,self.individualPursuitTimesWomen)
                self.addStartingLaps(data,self.startTimesIPWomens)


        elif filename.find('TeamPursuit'):
            self.addTimes(data,self.teamPursuitTimes)
            self.addStartingLaps(data,self.startTimesIP)
            if filename.find('Men')>0:
                self.addTimes(data,self.teamPursuitTimesMen)
                self.addStartingLaps(data,self.startTimesTPMens)
            else:
                self.addTimes(data,self.teamPursuitTimesWomen)
                self.addStartingLaps(data,self.startTimesTPMens)
                
        if filename.find('TeamSprint')>0:
            self.addTimes(data,self.teamSprint)
            self.addStartingLaps(data,self.startTimesTS)
            if filename.find('Men')>0:
                self.addTimes(data,self.teamSprintMens)
                self.addStartingLaps(data,self.startTimesTSMens)
                
            else:
                self.addTimes(data,self.teamSprintWomens)
                self.addStartingLaps(data,self.startTimesTSWomens)

                
    
            

        self.addStartingLaps(data,self.startTimes)
        


            


        
    def addTimes(self,data,addTo):
        for rider in data:
            perviousTime = datetime.strptime('00:00:00.000000','%H:%M:%S.%f')        
            for lap in rider['Laps']:
                lapTime = self.timeStrToTime(lap['time'])
                if lap['splitDistance']%250==0:
                    addTo.append(lapTime - perviousTime)
                    perviousTime = lapTime
    
    def addStartingLaps(self,data,addTo):
        for rider in data:
            perviousTime = datetime.strptime('00:00:00.000000','%H:%M:%S.%f')
            for lap in rider['Laps']:
                if lap['splitDistance']==250:
                    lapTime = self.timeStrToTime(lap['time'])
                    addTo.append(lapTime - perviousTime)
    

    def timeStrToTime(self,string):
        if len(string) == 8:
            timeObject= datetime.strptime(string,'%H:%M:%S')
        else:
            timeObject= datetime.strptime(string,'%H:%M:%S.%f')

        return timeObject


def main():
    st = SplitTime()
    print 'Number of Races:', len(sys.argv), 'files'
    for filename in sys.argv[1:]:
        #print filename
        st.readFile(filename)
                        
    print 'Average of All Times: '+str(sumTimeDeltas(st.allTimes)/len(st.allTimes))
    print 'Average of Mens Times: '+str(sumTimeDeltas(st.MensTimes)/len(st.MensTimes))
    print 'Average of Womens Times: '+str(sumTimeDeltas(st.WomensTimes)/len(st.WomensTimes))
    print ' '
    print 'Average of Team Times: '+str(sumTimeDeltas(st.teamTimes)/len(st.teamTimes))
    print 'Average of All Individual Times: '+str(sumTimeDeltas(st.individualTimes)/len(st.individualTimes))
    print  ' '
    print 'Average of IP Times: '+str(sumTimeDeltas(st.individualPursuitTimes)/len(st.individualPursuitTimes))
    print 'Average of IP mens solo times: '+str(sumTimeDeltas(st.individualPursuitTimesMen)/len(st.individualPursuitTimesMen))
    print 'Average of IP womens solo times: '+str(sumTimeDeltas(st.individualPursuitTimesWomen)/len(st.individualPursuitTimesWomen))
    print ' '
    print 'Average of team Pursuit Times: '+str(sumTimeDeltas(st.teamPursuitTimes)/len(st.teamPursuitTimes))
    print 'Average of TP Men '+str(sumTimeDeltas(st.teamPursuitTimesMen)/len(st.teamPursuitTimesMen))
    print 'Average of TP women times: '+str(sumTimeDeltas(st.teamPursuitTimesWomen)/len(st.teamPursuitTimesWomen))
    print ' '
    print 'Average of TeamSprint times: '+str(sumTimeDeltas(st.teamSprint)/len(st.teamSprint))
    print 'Average of TeamSprint Men times: '+str(sumTimeDeltas(st.teamSprint)/len(st.teamSprintMens))
    print 'Average of TeamSprint Women times: '+str(sumTimeDeltas(st.teamSprint)/len(st.teamSprintWomens))
    print ' '






def sumTimeDeltas(listOfTd):
    sumTD = timedelta()
    for x in listOfTd:
        sumTD+=x
    return sumTD


if __name__=="__main__":
    main()
