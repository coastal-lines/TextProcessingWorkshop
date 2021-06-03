from pyral import Rally, rallyWorkset
from Rally.TestsAndFoldersActions import TestsAndFoldersActions
import pickle
from bs4 import BeautifulSoup

#load test cases from file
def loadTestCasesFromFile():
    allTestCasesForSaveIntoFile = None
    with open(r'C:\Temp2\New folder\DataVisualizationAndStatisticsForRally\Draft\allTestCasesForSaveIntoFile.data', 'rb') as f:
        allTestCasesForSaveIntoFile = pickle.load(f)
    return allTestCasesForSaveIntoFile

def saveInputsIntoTextFile(listInputs):
    #removing some of extra characters
    position = -1
    for line in listInputs:
        position = position + 1

        if(line == '\xa0'):
            listInputs.pop(position)

        if('\xa0' in line):
            line = line.replace('\xa0', ' ')
            listInputs[position] = line

        #if('\n' in line):
         #   line = " ".join(line.splitlines())
          #  listInputs[position] = line

        tempLine = line.strip()
        if(len(tempLine) == 0):
            listInputs.pop(position)

    textfile = open(r"C:\Temp2\New folder\DataVisualizationAndStatisticsForRally\Draft\inputsListTxt.txt", "w")
    for element in listInputs:
        textfile.write(element + "\n")
    textfile.close()

#connect to rally, get all test cases, save into file
def preparingData():
    #read creads
    params = []
    with open(r'C:\Users\User\Desktop\!temp') as my_file:
        for line in my_file:
            params.append(line)

    #connection
    rally = Rally(server=params[0].rstrip(), user=params[1].rstrip(), password=params[2].rstrip())

    #set project and root folder
    rally.setWorkspace(params[3].rstrip())
    rally.setProject(params[4].rstrip())

    #get information from root folder
    testFolderRequest = rally.get('TestFolder', fetch=True, projectScopeDown=True, query='FormattedID = "' + params[5].rstrip() + '"')
    testFolder = testFolderRequest.next()

    #get all test cases inside of root folder
    allTestCasesForSaveIntoFile = TestsAndFoldersActions().extractTestCasesFromFoldersAndSubfolders(testFolder)

    #save test cases into file
    with open(r'C:\Temp2\New folder\DataVisualizationAndStatisticsForRally\Draft\allTestCasesForSaveIntoFile.data', 'w+b') as file:
        pickle.dump(allTestCasesForSaveIntoFile, file)
    print("Test cases were saved")

#extract text from html tags
def htmlParser(text):
    listInputs = []
    data = BeautifulSoup(text)

    parentTag = data.find("body").next.name

    allLi = data.find("body").findAll("li")
    allSpan = data.find("body").findAll("span")
    allDiv = data.find("body").findAll("div")
    allP = data.find("body").findAll("p")

    if (parentTag == "li" and allLi != []):
        for li in allLi:
            span = li.find_all("span")
            if (span != [] and span[0].text != ""):
                listInputs.append(li.getText())
                continue
            listInputs.append(li.text)

    elif (parentTag == "span" and allSpan != []):
        if(allDiv == []):
            for span in allSpan:
                u = data.findAll("u")
                strong = data.findAll("strong")
                if(u != [] or strong != []):
                    listInputs.append(data.getText())
                    break
                listInputs.append(span.text)

    elif (parentTag == "div" and allDiv != []):
        for div in allDiv:
            if(div.findAll("span") != []):
                listInputs.append(data.getText())
                break
            listInputs.append(div.text)

    elif (parentTag == "p" and allP != []):
            for p in allP:
                listInputs.append(p.text)

    elif(allLi == [] and allSpan == [] and allDiv == []):
        allP = data.find("body").findAll("p")
        for p in allP:
            listInputs.append(p.text)

    return listInputs

#prepare inputs list
def prepareInputsList(allTestCasesForSaveIntoFile):
    inputsList = []
    for tc in allTestCasesForSaveIntoFile:
        #inputsList.append(tc.formattedID)
        for input in tc.inputs:
            if("[AUTOMATED]" in tc.name):
                listOfInputsInsideOneStep = htmlParser(input)
                inputsList.extend(listOfInputsInsideOneStep)

    return inputsList

#preparingData()
allTestCasesForSaveIntoFile = loadTestCasesFromFile()
inputsList = prepareInputsList(allTestCasesForSaveIntoFile)
saveInputsIntoTextFile(inputsList)

