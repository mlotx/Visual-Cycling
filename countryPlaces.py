import csv
import json
from pprint import pprint
import sys
from datetime import datetime, timedelta

codeToCountry = {
    'CCT':'Japan',
    'HBC':'China',
    'NAV':'Spain',
    'HKP':'China',
    'RVL':'Russia',
    'FGN':'Spain',
    'HKG':'Hong Kong',
    'TPE':'Taiwan',
    'GIS':'New Zealand',
    'JAY':'Australia',
    'CHI':'Chile',
    'CHN':'China',
    'GPC':'China',
    'CAT':'Spain',
    'FIN':'Finland',
    'TCD':'Italy',
    'THA':'Thailand',
    'MAS':'Malaysia',
    'PHL':'Russia',
    'KAZ':'Kazakhstan',
    'GUA':'Guatemala',
    'BEL':'Belgium',
    'SKY':'Great Britan',
    'YSD':'Malaysia',
    'GBR':'Great Britan',
    'DEN':'Denmark',
    'GER':'Germany',
    'PTF':'Switzerland',
    'UGA':'Uganda',
    'TTA':'Kazakhstan',
    'GEO':'Georgia',
    'TRI':'Trinidad & Tobago',
    'BLR':'Belarus',
    'GRE':'Greece',
    'CGA':'Ireland',
    'IND':'India',
    'CZE':'Czech Republic',
    'BCN':'Trinidad & Tobago',
    'TMV':'Germany',
    'DOM':'Dominican Republic',
    'NED':'Netherlands',
    'SUI':'Switzerland',
    'CTF':'Italy',
    'COF':'France',
    'COL':'Columbia',
    'ISD':'Ukraine',
    'OUC':'U.S.A.',
    'ECU':'Ecuador',
    'LOK':'Russia',
    'FRA':'France',
    'WAL':'Great Britan',
    'LTU':'Lithuania',
    'DFT':'U.S.A.',
    'AUS':'Australia',
    'AUT':'Austria',
    'VEN':'Venezuela',
    'RDN':'Netherlands',
    'EUS':'Spain',
    'GDZ':'Poland',
    'ITA':'Italy',
    'RUS':'Russia',
    'MEX':'Mexico',
    'BRA':'Brazil',
    'USC':'France',
    'USA':'U.S.A.',	
    'TOS':'Australia',
    'UKR':'Ukraine',
    'MSP':'China',
    'ERD':'Germany',
    'CAN':'Canada',
    'KOR':'Korea',
    'UZB':'Uzbekistan',
    'POL':'Poland',
    'ESP':'Spain',
    'MTT':'Russia',
    'IRI':'Iran',
    'IRL':'Ireland',
    'HPM':'Great Britan',
    'KTA':'Russia',
    'NZL':'New Zealand',
    'JPN':'Japan',
    'KGZ':'Kyrgyzstan',
    'RSA':'South Africa',
    'ARG':'Argentina',
    'CUB':'Cuba'}

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
    GoldSilverBronzeDict = {}
    del st.CountryPlaceListDict['Time']
    del st.CountryPlaceListDict['2009']
    for country in st.CountryPlaceListDict:

        podiums = 0
        if codeToCountry[country] not in GoldSilverBronzeDict:
            GoldSilverBronzeDict[codeToCountry[country]] = {'Gold':0,'Silver':0,'Bronze':0}
        for result in st.CountryPlaceListDict[country]:
            if result is 1:
                GoldSilverBronzeDict[codeToCountry[country]]['Gold']+=1
            elif result is 2:
                GoldSilverBronzeDict[codeToCountry[country]]['Silver']+=1
            elif result is 3:
                GoldSilverBronzeDict[codeToCountry[country]]['Bronze']+=1
        if GoldSilverBronzeDict[codeToCountry[country]]['Bronze']==0 and GoldSilverBronzeDict[codeToCountry[country]]['Silver'] == 0 and GoldSilverBronzeDict[codeToCountry[country]]['Gold'] ==0:
            del GoldSilverBronzeDict[codeToCountry[country]]
            

    countryCSV = open('csvs/countrySuccess.csv','wb')
    countryWriter = csv.writer(countryCSV)
    countryWriter.writerow(['Country','Bronze','Silver','Gold'])
    for country in GoldSilverBronzeDict:
        countryWriter.writerow([country,GoldSilverBronzeDict[country]['Bronze'],GoldSilverBronzeDict[country]['Silver'],GoldSilverBronzeDict[country]['Gold']])



if __name__=="__main__":
    main()
