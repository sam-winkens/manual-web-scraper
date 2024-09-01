# milestone2.py
# cse in-class project
# Sam, 2023
import csv


def convertToDictionaries(keys: list, values: list):
    #keys is a list of strings
    #values is a list of lists
    outList = []
    outDict = {}
    for value in range(len(values)):
        for key in range(len(keys)):
            outDict[keys[key]] = values[value][key]
        outList.append(outDict)
        outDict = {}
    return outList

def loadRecords(filename):
    #takes in csv file
    outList = []
    with open(filename) as file:
        reader = csv.reader(file)
        for line in reader:
            outList.append(line)
        outList = outList[1:]
    return outList

def convertToLists(keys, lod):
    lol = []
    aList = []
    for dictionary in lod:
        for key in keys:
            aList.append(dictionary.get(key,''))
        lol.append(aList)
        aList = []
    return lol

def writeRecords(filename, records):
    #records is a list of lists
    with open(filename, 'a') as file:
        writer = csv.writer(file)
        for record in records:
            writer.writerow(record)