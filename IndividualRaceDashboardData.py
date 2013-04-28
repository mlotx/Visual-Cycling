import json
import sys
from datetime import datetime, timedelta
import operator
import csv
import glob

def timeStrToTime(string):
    if len(string) == 8:
        timeObject= datetime.strptime(string,'%H:%M:%S')
    else:
        timeObject= datetime.strptime(string,'%H:%M:%S.%f')

    return timeObject
                    


    

temp =  glob.glob("C:/Users/Maggie/Data Science/Project/*.json")
allfiles = []
for filename in temp[1:]:
    graphData = []
    personData = []
    print filename
                                 
    json_data=open(filename,'r')
    data = json.load(json_data)
    newfilename = filename.split("\\")[-1]
    newfilename = newfilename.rstrip('.json')
    print newfilename 
    for rider in data:
        country = rider['Country']
        team = 'Null'
        if 'Team' in rider.keys():
            team = rider['Team']
            
        place = []
        laptime = []
        currentLap =0
        totaltime = datetime.strptime('00:00:00.000000','%H:%M:%S.%f')
        pastTime = datetime.strptime('00:00:00.000000','%H:%M:%S.%f')
        zeroTime = datetime.strptime('00:00:00.000000','%H:%M:%S.%f')
        laps= rider['Laps']
        for lap in laps:
            if 'place' in lap.keys():
                if lap['place'] >0:
                    
                    
                    place.append(lap['place'])
                    temptime = timeStrToTime(lap['time'])
                    time = temptime - pastTime
                    if len(str(time)) ==7:
                            convertingtime = datetime.strptime(str (time)+'.000000','%H:%M:%S.%f')
                    else:
                            convertingtime = datetime.strptime(str (time),'%H:%M:%S.%f')
                    laptime.append(convertingtime)
                    pastTime = temptime
                    current = temptime - zeroTime
                    if len(str(current)) ==7:
                        totaltime = datetime.strptime(str (current)+'.000000','%H:%M:%S.%f')
                    else:
                        totaltime = datetime.strptime(str (current),'%H:%M:%S.%f')
                
        #graphData.append([place,laptime, totaltime])
        graphData.append(place)
        personData.append([country, team])
        #json.dump(writeList,r)
    tocsv = []
    first = []
    first.append('lap')
    for item in personData:
        first.append(item[0])
    tocsv.append(first)

    ifsomething =len(graphData)
    if ifsomething > 0:
        for x in range(len(graphData[0])):
            testLen =len(graphData[0])
            temp = []
            temp.append(x+1)
            for item in graphData:
                if len(item) == testLen:
                    
                    temp.append(item[x])
           
            tocsv.append(temp)
        
    
    allfiles.append(newfilename)   
    filename="IndividualRaceDashboardData\\"+ newfilename+".csv"
    with open(filename, 'wb') as f:
            writer = csv.writer(f)
            writer.writerows(tocsv)
print allfiles
   
                
        

    

