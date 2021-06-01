#read creads
params = []
with open(r'C:\Users\User\Desktop\!temp') as my_file:
    for line in my_file:
        params.append(line)

#serverText = params[0].rstrip()
#userText = params[1].rstrip()
#passwordText = params[2].rstrip()
#workspaceText = params[3].rstrip()
#projectText = params[4].rstrip()
#rootFolderText = params[5].rstrip() #TF15961 
#queryText = params[6].rstrip()

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

#load test cases from file
allTestCasesForSaveIntoFile = None
with open(r'C:\Temp2\New folder\DataVisualizationAndStatisticsForRally\Draft\allTestCasesForSaveIntoFile.data', 'rb') as f:
    allTestCasesForSaveIntoFile = pickle.load(f)

#create list of all Inputs
#remove html tags from inputs
inputsList = []
for tc in allTestCasesForSaveIntoFile:
    for input in tc.inputs:
        soup = BeautifulSoup(input)
        cleanText = ''.join(soup.findAll(text=True))
        inputsList.append(cleanText)
        print(cleanText)

#save input list into file
with open(r'C:\Temp2\New folder\DataVisualizationAndStatisticsForRally\Draft\inputsList.data', 'w+b') as file:
    pickle.dump(inputsList, file)