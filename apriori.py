import csv
import sys
import os.path
import csv
import math 
import types
from collections import defaultdict, Iterable
import itertools

class Apriori:
    """
    Totally borrowed this from David... mostly
    """
    def __init__(self, data, minSup, minConf):
        self.dataset = data
        #keeps track of individual persons
        #key = row #,
        #value = set(each feature for that person)
        self.transList = defaultdict(list)
        
        #frequency item list for itemsets of size 1
        #key = feature
        #value = frequency
        self.freqList = defaultdict(int)
        
        #contains all items sets of size 1, size 2, .... size k
        self.itemset = set()
        
        #total number of entries (ie total number of rows)
        self.numItems = 0
        
        #organize the data into dictionaries we can use and take counts of size 1
        self.prepData()
        
        #keeps track of item sets of any size that meet min support
            #key = # items in set
            #value = list of sets of size key that meet min support
        self.master_F = defaultdict(list)
        
        self.minSup = minSup
        self.minConf = minConf

    def prepData(self):
        key = 0
        #for each row in the data
        for bucket in self.dataset:
            #we have one more item
            self.numItems += 1
            
            #for each feature about each politicion
            for item in bucket:
                #append the dictionary stories each row
                self.transList[key].append(item.strip())
                #add to our set of unique items - only adds if it hasnt been seen before
                self.itemset.add(item.strip())
                #increment the tally for each item
                self.freqList[(item.strip())] += 1
                
            key+=1

    #generates all possible tuples that meat min support ie (a,b,c) or (a)
    def generate_Associations(self):
        candidate = {}
        count = {}
        
        self.master_F[1] = self.get_ones(self.freqList, 1)
        #now start making all the other combinations
        k = 2
        
        #while we are still generating combination
        while len(self.master_F[k-1]) != 0:
            print "Working on size: ", k
            #generate and store all candiates of size k from the candidates of size k-1
            candidate[k] = self.genCandidates(self.master_F[k-1], k)
        
            #count the number of rows our candidates are in by checking if the set version
                #of the candidate is a subset of the set version of the entire row
            for x in self.transList.iteritems():
                for c in candidate[k]:
                    if set(c).issubset(x[1]):
                        #c = sorted(c)
                        self.freqList[c] += 1
            self.master_F[k] = self.checkMinSup(candidate[k], k)
            k+=1
        for group in self.master_F.iterkeys():
            print 'Size ', group, ' found: ', len(self.master_F[group])
        return self.master_F

        
    def checkMinSup(self, items, k):
        local_f = []
        for item in items:
            count = self.freqList[item]
            support = self.support(count)
            if support >= self.minSup:
                local_f.append(item)
        return local_f
        
    def genSub(self, item):
        subsets = []
        
        #create all subsets with no repeated elements in each one
        for i in range(1, len(item)):
            subsets.extend(sorted(set(itertools.combinations(item, i))))
        return subsets
            
            
    #genereate more candidate pairs of size k from item pairs of size k-1
    #does not check min support requirement here... it is handled in the calling function instead
    def genCandidates(self, items, k):
        candidate = []
        
        #handle k = 2: generate all pairs of size 2 from every permuation of x and y that are not equal to eachother
        if k == 2:
            candidate = [tuple(sorted([x,y])) for x in items for y in items if len((x,y)) == k and x!=y]
        else:
            candidate = [tuple(sorted(set(x).union(y))) for x in items for y in items if len(set(x).union(y)) == k and x!=y]
            
            
        #eliminate duplicates and return result
        return set(candidate)
        
    #return the support of an item given its frequency
    def support(self, count):
        return float(count) / self.numItems
        
    def conf(self, subC, itemC):
        return float(itemC) / subC
        
    def get_ones(self, items, k):
        #store singles that meet min support
        local_F = []
        #for each item and its associated frequency count
        for item, count in items.iteritems():
            my_support = self.support(count)
            if my_support >= self.minSup:
                local_F.append(item)

        return local_F
        
    def makeRules(self, finished_F):
        Rules = []
        
        for k, itemset in finished_F.iteritems():
            if k >= 2:
                for item in itemset:
                    #item = sorted(item)
                    subsets = self.genSub(item)
                    for subset in subsets:
                        #subset = sorted(subset)
                        if len(subset) == 1:
                            subC = self.freqList[subset[0]]
                        else:
                            subC = self.freqList[subset]
                        itemC = self.freqList[item]
                        if subC != 0:
                            conf = self.conf(subC, itemC)
                            if conf >= self.minConf:
                                support = self.support(self.freqList[item])
                                follows = tuple(x for x in item if x not in subset)
                                if follows:
                                    Rules.append((subset, follows, self.freqList[item], support, subC, itemC, conf))
                                                            
        return Rules
                            




items = ['handicapped-infants',
'water-project-cost-sharing',
'adoption-of-the-budget-resolution', 
'physician-fee-freeze',
'el-salvador-aid',
'religious-groups-in-schools',
'anti-satellite-test-ban',
'aid-to-nicaraguan-contras', 
'mx-missile',
'immigration', 
'synfuels-corporation-cutback',
'education-spending',
'superfund-right-to-sue', 
'crime',
'duty-free-exports',
'export-administration-act-south-africa']


def main():
    dataset = csv.reader(open("csvs/womenTP.csv", "r"))
    goods = defaultdict(list)
    minSup = 0.07
    minConf = .6
    
        
    a = Apriori(dataset, minSup, minConf)
    finalItemsets = a.generate_Associations()
    
    count = 0
    rules = a.makeRules(finalItemsets)
    cur_max = 0
    maxsupport = 0
    for rule in rules:
        local_max = len(rule[0]) + len(rule[1])
        if local_max > cur_max:
            cur_max = local_max
        count += 1
        if float(rule[3])>maxsupport:
            maxsupport=float(rule[3])
        print count, " Rule: ", rule[0], " --> ", rule[1]
        print '\t Frequency: ', rule[2]
        print '\t Support: ', rule[3]
        print '\t Conf Num: ', rule[5]
        print '\t Conf Den: ', rule[4]
        print '\t Conf: ', rule[6]

    print 'Longest rule length: ', cur_max
    print 'max support: '+str(maxsupport)

if __name__=="__main__":
    main()

