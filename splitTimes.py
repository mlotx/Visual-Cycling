import json
from pprint import pprint
import sys

class SplitTime():
    def __init__(self):
        self.allTimes = []
        self.MensTimes = []
        self.WomensTimes = []
        self.PursuitTimes = []
        self.startTimes = []
        self.TeamSprintTimes = []
        
    def readFile(self,filename):
        json_data=open(filename,'r')
        data = json.load(json_data)
        pprint(data)
        json_data.close()


def main():
    st = SplitTime()
    print 'Number of Races:', len(sys.argv), 'files'
    for filename in sys.argv[1:]:
        print filename
        st.readFile(filename)
                        
        

if __name__=="__main__":
    main()
