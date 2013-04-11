from datetime import time
import pprint
import json
import sys
pp = pprint.PrettyPrinter(indent=4)

class TimeParsing:
    def individual(self,filename, writeFilename):
        f = open(filename, 'r')
        r = open(writeFilename,'w')
        for line in f:
            if ('Heat' in line) or ('BRONZE' in line) or ('GOLD' in line):
                line = line.rstrip('\n')
                temp = f.next()
                racers = []
                while 'Distance' not in temp:
                    temp = temp.rstrip('\n')
                    if len(temp) > 8:
                        racers.append(temp)

                    temp = f.next()
        
                for person in range (0, len(racers)):
                    JSON = {}
                    rider = racers[person].split()
                    JSON['lastName'] = rider[1]
                    if len(rider) >5:
                        JSON['firstName'] = rider[3]
                    else:
                        JSON['firstName'] = rider[2]
                    JSON['Country'] = rider.pop()
                    JSON['Laps']=[]
                    newtemp = f.next()
                    newtemp = newtemp.rstrip('\n')
                    write = True
                    while 'Distance' not in newtemp and len(newtemp) >2:
                        if 'DNF' in newtemp or 'DNS' in newtemp or 'REL' in newtemp or 'DSQ' in newtemp or 'OVL' in newtemp or len(newtemp)<10:
                            write = False
                        if write:
                            newtemp = newtemp.rstrip('\n')
                            newtemp = newtemp.split()
                            newtemp[0] = int(newtemp[0][:-1])
                            if newtemp[1].find(':')>0:
                                newtemp[1] = time(0,
                                                 int(newtemp[1][0:newtemp[1].find(':')]),
                                                  int(newtemp[1][newtemp[1].find(':')+1:newtemp[1].find('.')]),
                                                  int(newtemp[1][newtemp[1].find('.')+1:])*1000)
                            else:
                                newtemp[1] = time(0,
                                                  0,
                                                  int(newtemp[1][newtemp[1].find(':')+1:newtemp[1].find('.')]),
                                                  int(newtemp[1][newtemp[1].find('.')+1:])*1000)
                            if len(newtemp)==4:
                                newtemp[2] = int(newtemp[2])
                            elif len(newtemp)==3:
                                newtemp[2]=-1
                            else:
                                newtemp.append(-1)

                            if len(newtemp) is 4:
                                newtemp.pop()
                            JSON['Laps'].append({'splitDistance':newtemp[0],
                                                'time':str(newtemp[1]),
                                                'place':newtemp[2]}) 

                        newtemp = f.next()

                    if write:
                        json.dump(JSON,r)       
        f.close()
        r.close()                        
                            
    def team(self,filename, writeFilename):
        f = open(filename, 'r')
        r = open(writeFilename,'w')
        for line in f:
            if ('Heat' in line) or ('BRONZE' in line) or ('GOLD' in line):
                line = line.rstrip('\n')
                temp = f.next()
                racers = []
                while 'Distance' not in temp:
                    temp = temp.rstrip('\n')
                    if len(temp) > 8:
                        racers.append(temp)

                    temp = f.next()
        
                for person in range (0, len(racers)):
                    JSON = {}
                    rider = racers[person].split('\xc2\xad')
                    rider[1] = rider[1].strip()
                    JSON['Team'] = rider[1]
                    JSON['Country'] = rider[0]
                    JSON['Laps']=[]
                    newtemp = f.next()
                    newtemp = newtemp.rstrip('\n')
                    write = True 
                    while 'Distance' not in newtemp and len(newtemp) >2:
                        if 'DNF' in newtemp or 'DNS' in newtemp or 'REL' in newtemp or 'DSQ' in newtemp or 'OVL' in newtemp or len(newtemp)<10:
                            write = False
                        if write:
                            newtemp = newtemp.rstrip('\n')
                            newtemp = newtemp.split()
                            newtemp[0] = int(newtemp[0][:-1])
                            if newtemp[1].find(':')>0:
                                newtemp[1] = time(0,
                                                 int(newtemp[1][0:newtemp[1].find(':')]),
                                                  int(newtemp[1][newtemp[1].find(':')+1:newtemp[1].find('.')]),
                                                  int(newtemp[1][newtemp[1].find('.')+1:])*1000)
                            else:
                                newtemp[1] = time(0,
                                                  0,
                                                  int(newtemp[1][newtemp[1].find(':')+1:newtemp[1].find('.')]),
                                                  int(newtemp[1][newtemp[1].find('.')+1:])*1000)
                            if len(newtemp)==4:
                                newtemp[2] = int(newtemp[2])
                            elif len(newtemp)==3:
                                newtemp[2]=-1
                            else:
                                newtemp.append(-1)
                            if len(newtemp) is 4:
                                newtemp.pop()
                            JSON['Laps'].append({'splitDistance':newtemp[0],
                                                'time':str(newtemp[1]),
                                                'place':newtemp[2]}) 

                        newtemp = f.next()

                    if write:
                        json.dump(JSON,r)            
        f.close()
        r.close()             
        

def main():
    print 'Number of files:', len(sys.argv), 'files'
    for filename in sys.argv:
        print filename
        parser = TimeParsing()
        if filename.find('.py') == -1:
            writeFilename = filename.replace('.txt','.json').replace('texts','jsons').replace('/Type 1','')
            print writeFilename

            if filename.find('Team')>0:
                parser.team(filename, writeFilename)
            else:
                parser.individual(filename, writeFilename)
            
        

if __name__=="__main__":
    main()
