__author__ = 'titan'
'''
Author: Perry Jones (6661564)
Date: 10/31/2015

##################################################################################################################
#Role:                                                                                                           #
#This script retreives the ranges of alexa domains to analyze then calls dispatcher to process the domains under #
#question.                                                                                                       #
##################################################################################################################
'''

import hashlib

AlexaFileLocation="top-1m.csv"

#Converted java function to python for alexa domain start selection
def getStartIndex(studentId):
    md = hashlib.sha256()
    md.update(str(studentId))
    return ((int(md.hexdigest(),16)%9890)*100)+1000

def loadAlexaDomains(alexaFile,offset):
    domains = []
    alexa=open(alexaFile)
    line=alexa.readline()
    counter=1
    end=offset+9999
    while line:
        if (counter>=offset) and (counter <=end):
            domains.append(line.split(","))
        line=alexa.readline()
        counter +=1
    return domains

def main():
    global AlexaFileLocation
    studentId = 6661564
    startLocation = getStartIndex(studentId)
    domainsToQuery = loadAlexaDomains(AlexaFileLocation,startLocation)
    print domainsToQuery[0],domainsToQuery[:-1]


if __name__ == "__main__":
    main()
