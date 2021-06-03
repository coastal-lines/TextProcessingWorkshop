from pyral import Rally, rallyWorkset
from Rally.TestsAndFoldersActions import TestsAndFoldersActions
import pickle
from bs4 import BeautifulSoup

#
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

def saveLikeAText(listInputs):
    textfile = open(r"C:\Temp2\New folder\DataVisualizationAndStatisticsForRally\Draft\inputsListTxt.txt", "w")
    for element in listInputs:
        textfile.write(element + "\n")
    textfile.close()

def htmlParser(text):
    listInputs = []
    data = BeautifulSoup(text)

    allLi = data.find("body").findAll("li")
    allSpan = data.find("body").findAll("span")
    allDiv = data.find("body").findAll("div")

    if (allLi != []):
        for li in allLi:
            span = li.find_all("span")
            if (span != [] and span[0].text != ""):
                listInputs.append(li.getText())
                continue
            listInputs.append(li.text)

    elif (allSpan != []):
        for span in allSpan:
            listInputs.append(span.text)

    elif (allDiv != []):
        for div in allDiv:
            listInputs.append(div.text)

    elif(allLi == [] and allSpan == [] and allDiv == []):
        allP = data.find("body").findAll("p")
        for p in allP:
            listInputs.append(p.text)

    return listInputs

#preparingData()

#load test cases from file
allTestCasesForSaveIntoFile = None
with open(r'C:\Temp2\New folder\DataVisualizationAndStatisticsForRally\Draft\allTestCasesForSaveIntoFile.data', 'rb') as f:
    allTestCasesForSaveIntoFile = pickle.load(f)