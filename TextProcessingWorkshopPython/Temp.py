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
    testFolderRequest = rally.get('TestFolder', fetch=True, projectScopeDown=True, query='FormattedID = "' + "TF18438" + '"')
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

    #find all <li>
    allLi = data.find("body").findAll("li")
    for li in allLi:
        listInputs.append(li.text)

    #span
    allSpan = data.find("body").findAll("span")
    for span in allSpan:
        listInputs.append(span.text)

    #div
    allDiv = data.find("body").findAll("div")
    for div in allDiv:
        listInputs.append(div.text)

    #if():
     #   listInputs.append(text)

    return listInputs

#preparingData()

#load test cases from file
allTestCasesForSaveIntoFile = None
with open(r'C:\Temp2\New folder\DataVisualizationAndStatisticsForRally\Draft\allTestCasesForSaveIntoFile.data', 'rb') as f:
    allTestCasesForSaveIntoFile = pickle.load(f)

#create list of all Inputs
#remove html tags from inputs
inputsList = []
for tc in allTestCasesForSaveIntoFile:
    for input in tc.inputs:
        listOfInputsInsideOneStep = htmlParser(input)
        
        soup = BeautifulSoup(input)
        cleanText = ''.join(soup.findAll(text=True))
        cleanText = cleanText.replace(u'\xa0', ' ')
        #splittedLines = []
        #if('\n' in cleanText):
            #   #splitString(cleanText)
          #  splittedLines = cleanText.splitlines()
         #   inputsList.append(splittedLines)
        inputsList.append(cleanText)
        inputsList.extend(listOfInputsInsideOneStep)
        #print(cleanText)

saveLikeAText(inputsList)

#save input list into file
#with open(r'C:\Temp2\New folder\DataVisualizationAndStatisticsForRally\Draft\inputsList.data', 'w+b') as file:
 #   pickle.dump(inputsList, file)

#72 lines should be