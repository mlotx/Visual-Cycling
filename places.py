import json
from pprint import pprint
import sys
from datetime import datetime, timedelta
import csv
import unicodedata

class Places():
    def __init__(self):
        menTP = open('csvs/menTP.csv','wb')
        self.menTPWriter = csv.writer(menTP)

        womenTP = open('csvs/womenTP.csv','wb')
        self.womenTPWriter = csv.writer(womenTP)

        menIP = open('csvs/menIP.csv','wb')
        self.menIPWriter = csv.writer(menIP)

        womenIP = open('csvs/womenIP.csv','wb')
        self.womenIPWriter = csv.writer(womenIP)

        menTS = open('csvs/menTS.csv','wb')
        self.menTSWriter = csv.writer(menTS)

        womenTS = open('csvs/womenTS.csv','wb')
        self.womenTSWriter = csv.writer(womenTS)
        
        menKilo = open('csvs/menKilo.csv','wb')
        self.menKiloWriter = csv.writer(menKilo)
        
            
    def DoStuff(self,filename):
        json_data=open(filename,'r')
        data = json.load(json_data)
        csvFile = open(filename.replace('json','csv'),'wb')
        csvWriter = csv.writer(csvFile)
        toFile = []
        for racer in data:
            tmp=[]
            if filename.find('Team')>0:
                team = racer['Team'].replace(' ','')
                tmp.append(unicodedata.normalize('NFKD', team ).encode('ascii','ignore'))
            else:
                tmpString = racer['firstName']+racer['lastName']
                tmpString.replace(' ','')
                tmp.append(unicodedata.normalize('NFKD', tmpString).encode('ascii','ignore'))

            for lap in racer['Laps']:
                if lap['splitDistance']%250==0:
                    try:
                        tmp.append(int(lap['place']))
                    except:
                        tmp=[]
                        break;
            if len(tmp)>0:
                toFile.append(tmp)    
        csvWriter.writerows(toFile)

        if filename.find('MensTeamPursuit')>0:
            self.WriteTheData(self.menTPWriter,toFile)

        elif filename.find('WomensTeamPursuit')>0:
            self.WriteTheData(self.womenTPWriter,toFile)

        elif filename.find('MensIndividualPursuit')>0:
            self.WriteTheData(self.menIPWriter,toFile)

        elif filename.find('WomensIndividualPursuit')>0:
            self.WriteTheData(self.womenIPWriter,toFile)

        elif filename.find('MensTeamSprint')>0:
            self.WriteTheData(self.menTSWriter,toFile)

        elif filename.find('WomensTeamSprint')>0:
            self.WriteTheData(self.womenTSWriter,toFile)

        elif filename.find('Kilo')>0:
            self.WriteTheData(self.menKiloWriter,toFile)
        
    def WriteTheData(self,writer,writeData):
        for x in writeData:
            count = 1
            while (count<len(x)):
                x[count] = 'Lap-'+str(count)+'-Place-'+str(x[count])
                count+=1
            writer.writerow(x)


        

def main():
    st = Places()
    print 'Number of Races:', len(sys.argv), 'files'
    for filename in sys.argv[1:]:
        if filename.find('Qual')>0 or filename.find('Kilo')>0:
            print filename
            st.DoStuff(filename)

if __name__=="__main__":
    main()
