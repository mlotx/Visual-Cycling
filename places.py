import json
from pprint import pprint
import sys
from datetime import datetime, timedelta


class Places():
    def __init__(self):
        self.CountryPlaceListDict={}
        self.ListofDifferentPlacings = []
                
    def readFile(self,filename):
        json_data=open(filename,'r')
        data = json.load(json_data)
        self.countryResults(data)

    def countryResults(self,data):
        for rider in data:
            place = self.getFinal(rider['Laps'])
            if place:
                if rider['Country'].strip() in self.CountryPlaceListDict:
                    self.CountryPlaceListDict[rider['Country'].strip()].append(place)
                else:
                    self.CountryPlaceListDict[rider['Country'].strip()] = [place]
                
    def getFinal(self,laps):
        place = 100000
        longest = 0
        for lap in laps:
            if lap['splitDistance']>longest and 'place' in lap and lap['place'] != -1 :
                longest = lap['splitDistance']
                try:
                    place = int(lap['place'])
                except:
                    return None
        if place == 100000:
            return None
        else:
            return place


def main():
    st = Places()
    print 'Number of Races:', len(sys.argv), 'files'
    for filename in sys.argv[1:]:
        #print filename
        st.readFile(filename)
    
    pprint(st.CountryPlaceListDict)

if __name__=="__main__":
    main()
