# milestone1.py
# cse in-class project
# Sam, 2023

data = [{'Title': 'SOLE PARK', 'Category': 'SCULPTURE', 'Type': 'RELIEF',
         'Medium': 'STONE', 'Frame': 'false', 'Photo URL Link': 'UNKNOWN', 'Artist':
             'UNKNOWN', 'Street Address': 'BUSTI AVE & NIAGARA ST', 'City': 'BUFFALO',
         'Zipcode': '14213', 'State': 'NY'},
        {'Title': 'BUFFALO STREET MAP', 'Category': 'GRAPHIC ARTS', 'Type': 'MAP',
         'Medium': 'PARCHMENT', 'Frame': 'true', 'Photo URL Link': 'UNKNOWN',
         'Artist': 'SMITH BROTHERS COMPANY', 'Street Address': '65 NIAGARA SQUARE',
         'City': 'BUFFALO', 'Zipcode': '14202', 'State': 'NY'},
        {'Title': 'WAR MEMORIAL STADIUM RENDERING', 'Category': 'GRAPHIC ARTS',
         'Type': 'DRAWING', 'Medium': 'PAPER', 'Frame': 'false', 'Photo URL Link':
             'UNKNOWN', 'Artist': 'UNKNOWN', 'Street Address': '65 NIAGARA SQUARE',
         'City': 'BUFFALO', 'Zipcode': '14202', 'State': 'NY'},
        {'Title': 'MAYOR HIRAM BARTON', 'Category': 'PAINTINGS', 'Type': 'PORTRAIT',
         'Medium': 'OIL ON CANVAS', 'Frame': 'true', 'Photo URL Link':
             'HTTP://WWW.CI.BUFFALO.NY.US/FILES/1_2_1/PUBLIC%20ART%20WEBSITE/WEB%20PAGES/HIRAM%20BARTON.HTML',
         'Artist': 'UNKNOWN', 'Street Address': '65 NIAGARA SQUARE', 'City': 'BUFFALO', 'Zipcode': '14202',
         'State': 'NY'},
        {'Title': 'MAYOR ELI COOK', 'Category': 'GRAPHICS ARTS', 'Type': 'PORTRAIT',
         'Medium': 'PASTEL ON PAPER', 'Frame': 'true', 'Photo URL Link':
             'HTTP://WWW.CI.BUFFALO.NY.US/FILES/1_2_1/PUBLIC%20ART%20WEBSITE/WEB%20PAGES/ELI%20COOK.HTML',
         'Artist': 'UNKNOWN', 'Street Address': '65 NIAGARA SQUARE',
         'City': 'BUFFALO', 'Zipcode': '14202', 'State': 'NY'},
        {'Title': 'MAYOR ANTHONY MASIELLO', 'Category': 'PAINTINGS', 'Type':
            'PORTRAIT', 'Medium': 'OIL ON CANVAS', 'Frame': 'true', 'Photo URL Link':
             'UNKNOWN', 'Artist': 'NATHAN NAETZKER', 'Street Address': '65 NIAGARA SQUARE', 'City': 'BUFFALO',
         'Zipcode': '14202', 'State': 'NY'},
        {'Title': 'MAYOR CHANDLER J WELLS', 'Category': 'PAINTINGS', 'Type':
            'PORTRAIT', 'Medium': 'OIL ON CANVAS', 'Frame': 'true', 'Photo URL Link':
             'HTTP://WWW.CI.BUFFALO.NY.US/FILES/1_2_1/PUBLIC%20ART%20WEBSITE/WEB%20PAGES/CHANDLER%20WELLS.HTML',
         'Artist': 'ALVAH BRADISH', 'Street Address': '65 NIAGARA SQUARE', 'City': 'BUFFALO', 'Zipcode': '14202',
         'State': 'NY'},
        {'Title': 'MAYOR CHANDLER J WELLS', 'Category': 'PAINTINGS', 'Type':
            'PORTRAIT', 'Medium': 'OIL ON CANVAS', 'Frame': 'true', 'Photo URL Link':
             'HTTP://WWW.CI.BUFFALO.NY.US/FILES/1_2_1/PUBLIC%20ART%20WEBSITE/WEB%20PAGES/CHANDLER%20WELLS.HTML',
         'Artist': 'ALVAH BRADISH', 'Street Address': '65 NIAGARA SQUARE', 'City': 'BUFFALO', 'Zipcode': '14202',
         'State': 'NY'}
        ]

def getValuesForKey(key: str, records: list) -> list:
    valuesList = [] #using an accumulator pattern
    for dictionary in records:
        keyValue = dictionary.get(key, 'None')
        if keyValue != 'None':
            if keyValue not in valuesList:
                valuesList.append(keyValue)
    return valuesList

def countMatchesByKey(key: str, value: str, records: list) -> int:
    count = 0 #using an accumulator pattern
    for dictionary in records:
        keyValue = dictionary.get(key, 'None')
        if keyValue != 'None':
            if keyValue == value:
                count += 1
    return count

def countMatchesByKeys(key1: str, value1: str, key2: str, value2: str, records: list) -> int:
    count = 0 #using an accumulator pattern
    for dictionary in records:
        keyValue1 = dictionary.get(key1, 'None')
        keyValue2 = dictionary.get(key2, 'None')
        if keyValue1 != 'None' and keyValue2 != 'None':
            if keyValue1 == value1 and keyValue2 == value2:
                count += 1
    return count

def filterByKey(key: str, value: str, records: list) -> list:
    dictionaryList = [] #using an accumulator pattern
    for dictionary in records:
        keyValue = dictionary.get(key, 'None')
        if keyValue != 'None':
            if keyValue == value:
                dictionaryList.append(dictionary)
    return dictionaryList

def computeFrequency(key: str, records: list) -> dict:
    newDict = {} #using an accumulator pattern
    for dictionary in records:
        keyValue = dictionary.get(key, 'None')
        if keyValue != 'None':
            if keyValue not in newDict:
                newDict[keyValue] = 1
            else:
                newDict[keyValue] += 1
    return newDict