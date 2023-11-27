import csv
import json

def parseRange(range):
    lengthRange = len(range)
    match lengthRange:
        case 1:
            return int(range)
        case 2:
            return int(range)
        case 3:
            return (int(range[0]),int(range[2]))
        case 5:
            return (int(range[:2]),int(range[3:5]))
        

def make_json(csvFilePath, jsonFilePath):
     
    # create a dictionary
    dataPrimary = {}
    dataSecondary = {}
     
    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        
        # Convert each row into a dictionary 
        # and add it to data
        for rows in csvReader:
            # if rows['CR'] != PrimaryKey:
            #     dataSecondary = {}

            # Assuming a column named 'No' to
            # be the primary key
            PrimaryKey = rows['CR']
            SecondaryKey = rows['d100']
            rollRange = parseRange(SecondaryKey)
            tempCounter = 0
            if (type(rollRange)) == tuple:
                # print("Tuple Values:", rollRange[0], "and", rollRange[1])
                if rollRange[1] == 0 or rollRange[0] == 0:
                    tempCounter += 1
                # print(tempCounter)
            else:
                # print('Int Value:', rollRange)
                if rollRange == 0:
                    tempCounter += 1
            # if list(dataSecondary)[-1] != list(dataSecondary)[0]:
            #     dataSecondary = {}
            #     dataSecondary[SecondaryKey] = rows
            dataSecondary[SecondaryKey] = rows
            dataPrimary[PrimaryKey] = dataSecondary
            if tempCounter == 1:
                dataSecondary = {}
                print(rows)

        # print(dataPrimary)

    # Open a json writer, and use the json.dumps() 
    # function to dump data
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(dataPrimary, indent=4))

csvFile = 'HoardLootTable - Sheet1.csv'
jsonFile = 'LootTables/LootTableList.json'

make_json(csvFile,jsonFile)