from datetime import time
import pprint
import json
import sys
pp = pprint.PrettyPrinter(indent=4)

class TimeParsing:
    def individual(self,filename, writeFilename):
        f = open(filename, 'r')
        r = open(writeFilename,'w')
        writeList=[]
        currentRiders = []
        for line in f:
            if line[:2]=="No":
                JSON={}
                rider = line.split()
                rider.pop(0)
                rider.pop(0)
                rider.pop(0)
                JSON['Country'] = rider.pop().replace('(','').replace(')','')
                JSON['firstName'] = rider.pop()
                JSON['lastName'] = ''
                for name in rider:
                    JSON['lastName'] += name + ' '
                JSON['lastName'] = JSON['lastName'].strip()
                JSON['Laps']=[]                            
                currentRiders.append(JSON);

            elif '125m' in line and len(line)> 6:
                JSON = currentRiders.pop(0)
                write = True
                while  len(line) > 4:
                    lap = {}
                    lapData = line.split()
                    if len(lapData)==1:
                        write = False
                        break
                    lap['splitDistance'] = int(lapData[0][:-1])
                    if lapData[1].find(':')>0:
                        lap['time'] = str(time(0,
                                          int(lapData[1][0:lapData[1].find(':')]),
                                          int(lapData[1][lapData[1].find(':')+1:lapData[1].find('.')]),
                                          int(lapData[1][lapData[1].find('.')+1:])*1000))
                    elif lapData[1].find('.')>0:
                        lap['time'] = str(time(0,
                                               0,
                                               int(lapData[1][lapData[1].find(':')+1:lapData[1].find('.')]),
                                               int(lapData[1][lapData[1].find('.')+1:])*1000))
                    else:
                        write = False
                        break
                    if len(lapData)>2:
                        lap['place'] = lapData[2]
                    JSON['Laps'].append(lap)

                    line = f.next()
                if write:
                    writeList.append(JSON)
        f.close()
        json.dump(writeList,r)       
        r.close()                        
                            
    def team(self,filename, writeFilename):
        f = open(filename, 'r')
        r = open(writeFilename,'w')
        writeList=[]
        currentRiders = []
        for line in f:
            if line[:2]=="No":
                JSON={}
                rider = line.split()
                rider.pop(0)
                rider.pop(0)
                rider.pop(0)
                JSON['Country'] = rider.pop().replace('(','').replace(')','')
                JSON['Team'] = ''
                for name in rider:
                    JSON['Team'] += name + ' '
                JSON['Team'] = JSON['Team'].strip()
                JSON['Laps']=[]                            
                currentRiders.append(JSON);

            elif '125m' in line and len(line)> 6:
                JSON = currentRiders.pop(0)
                write = True
                while  len(line) > 4:
                    lap = {}
                    lapData = line.split()
                    if len(lapData)==1:
                        write = False
                        break
                    lap['splitDistance'] = int(lapData[0][:-1])
                    if lapData[1].find(':')>0:
                        lap['time'] = str(time(0,
                                          int(lapData[1][0:lapData[1].find(':')]),
                                          int(lapData[1][lapData[1].find(':')+1:lapData[1].find('.')]),
                                          int(lapData[1][lapData[1].find('.')+1:])*1000))
                    elif lapData[1].find('.')>0:
                        lap['time'] = str(time(0,
                                               0,
                                               int(lapData[1][lapData[1].find(':')+1:lapData[1].find('.')]),
                                               int(lapData[1][lapData[1].find('.')+1:])*1000))
                    else:
                        write = False
                        break
                    if len(lapData)>2:
                        lap['place'] = lapData[2]
                    JSON['Laps'].append(lap)

                    line = f.next()
                if write:
                    writeList.append(JSON)
                else:
                    print filename
        f.close()
        json.dump(writeList,r)        
        r.close()                      
        

def main():
    print 'Number of files:', len(sys.argv), 'files'
    for filename in sys.argv:
        #print filename
        parser = TimeParsing()
        if filename.find('.py') == -1:
            writeFilename = filename.replace('.txt','.json').replace('texts','jsons').replace('/Type 2','')
            #print writeFilename

            if filename.find('Team')>0:
                parser.team(filename, writeFilename)
            else:
                parser.individual(filename, writeFilename)
            
        

if __name__=="__main__":
    main()
