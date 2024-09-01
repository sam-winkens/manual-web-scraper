# milestone3.py
# cse in-class project
# Sam, 2023

import milestone1
import milestone2
import os
import json
import urllib.request as ur
import csv
import matplotlib.pyplot as plt

def writeHeader(keys, filename):
    with open(filename, 'w') as fp:
        writer = csv.writer(fp)
        writer.writerow(keys)

def cacheAndLoadData(filename):
    keys = ['title', 'category', 'type', 'medium', 'frame', 'photo_url_link', 'artist',
            'site', 'street_address', 'city', 'zip_code', 'state', 'latitude', 'longitude']
    if not os.path.isfile(filename):
        url = 'https://data.buffalony.gov/resource/6xz2-syui.json'
        response = ur.urlopen(url)
        content_string = response.read().decode()
        content = json.loads(content_string)
        lod = []
        for aList in content:
            lod.append(aList)
        lol = milestone2.convertToLists(keys, lod)
        writeHeader(keys, filename)
        milestone2.writeRecords(filename, lol)

    newLOL = milestone2.loadRecords(filename)
    newLOD = milestone2.convertToDictionaries(keys, newLOL)
    return newLOD

def cleanData(data):
    for dictionary in data:
        if dictionary['category'] == 'PAINTINGS':
            dictionary['category'] = 'PAINTING'
        elif dictionary['category'] == 'DECORATIVE OBJECTS':
            dictionary['category'] = 'DECORATIVE OBJECT'
        elif dictionary['category'] == 'GRAPHIC' or dictionary['category'] == 'GRAPHICS' or dictionary['category'] == 'GRAPHICS ARTS':
            dictionary['category'] = 'GRAPHIC ARTS'

def plotPieForKey(key, data):
    computedFrequency = milestone1.computeFrequency(key, data)
    #create pie chart
    dataSize = list(computedFrequency.values())
    dataLabels = list(computedFrequency.keys())
    plt.pie(dataSize, labels=dataLabels)
    plt.show()

def plotBarForKey(key, data):
    computedFrequency = milestone1.computeFrequency(key, data)
    #create bar chart
    dataSize = list(computedFrequency.values())
    dataLabels = list(computedFrequency.keys())
    plt.barh(dataLabels, dataSize)
    plt.show()

def plotFilterBarForKey(key, fkey, fval, data):
    filteredData = milestone1.filterByKey(fkey, fval, data)
    computedFrequency = milestone1.computeFrequency(key, filteredData)
    dataSize = list(computedFrequency.values())
    dataLabels = list(computedFrequency.keys())
    plt.barh(dataLabels, dataSize)
    plt.show()

