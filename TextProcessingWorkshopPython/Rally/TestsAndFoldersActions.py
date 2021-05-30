from Rally.RallyTestCase import TestCase

class TestsAndFoldersActions():
    allTestCasesInFolderIncludeSubfolders = []
    allTC = []
    listTC = []

    @staticmethod
    def extractTestCasesFromFoldersAndSubfolders(rootFolder):
        listTestCases = []
        #TestsAndFoldersActions.allTC = None #Debug?

        if len(rootFolder.TestCases) > 0:
            TestsAndFoldersActions.extractTestCasesFromRootFolder(rootFolder)
            TestsAndFoldersActions.allTestCasesInFolderIncludeSubfolders.clear()

        if len(rootFolder.Children) > 0:
            for folder in rootFolder.Children:
                TestsAndFoldersActions.extractTestCasesFromFolder(folder)
                TestsAndFoldersActions.allTestCasesInFolderIncludeSubfolders.clear()

        for testCase in TestsAndFoldersActions.allTC:
            formattedID = testCase.FormattedID
            name = testCase.Name
            preConditions = testCase.PreConditions
            rootFolderName = rootFolder.Name
            project = testCase.Project.Name
            productArea = testCase.c_ProductArea
            productSubarea = testCase.c_ProductSubarea
            method = testCase.Method
            testFolder = testCase.TestFolder.Name

            mainFolderName = ""
            for rootFolder in rootFolder.Children:
                if testCase.TestFolder.Name == rootFolder.Name:
                    mainFolderName = rootFolder.Name
                    break
                elif testCase.TestFolder.Parent.Name == rootFolder.Name:
                    mainFolderName = testCasec.TestFolder.Parent.Name
                    break
                else:
                    tf = testCase.TestFolder.Parent
                    mainFolderName = TestsAndFoldersActions.getParentName(tf, rootFolder.Name)
            
            inputs  = []
            expecteds = []

            list_steps = testCase.Steps
            for i in list_steps:
                inputs.append(i.Input)
                expecteds.append(i.ExpectedResult)

            if testCase.Name.find("AUTOMATED") != -1 or testCase.Name.find("Automated") != -1:
                isAutomated = True
            else:
                isAutomated = False

            listTestCases.append(TestCase(formattedID, name, preConditions, inputs, expecteds, mainFolderName, rootFolderName, project, productArea, productSubarea, method, testFolder, isAutomated))

        return listTestCases

    @staticmethod
    def extractTestCasesFromRootFolder(folder):
        if len(folder.TestCases) > 0:
            for testCase in folder.TestCases: 
                print(testCase.Name)
                TestsAndFoldersActions.allTestCasesInFolderIncludeSubfolders.append(testCase)
                TestsAndFoldersActions.allTC.append(testCase)

    @staticmethod
    def extractTestCasesFromFolder(folder):
        if len(folder.TestCases) > 0:
            for testCase in folder.TestCases: 
                print(testCase.Name)
                TestsAndFoldersActions.allTestCasesInFolderIncludeSubfolders.append(testCase)
                TestsAndFoldersActions.allTC.append(testCase)
        if len(folder.Children) > 0:
            TestsAndFoldersActions.extractFolders(folder.Children)

    @staticmethod
    def extractFolders(folders):
        for folder in folders:
            print(folder.Name)
            print("---")
            TestsAndFoldersActions.extractTestCasesFromFolder(folder)

    #find parent name by recursion
    @classmethod
    def getParentName(cls, testFolder, rootFolderName):
        try:
            if testFolder.Name != None and testFolder.Name == rootFolderName:
                return rootFolderName
            else:
                TestsAndFoldersActions.getParentName(testFolder.Parent, rootFolderName)
        except AttributeError:
            print("not this root folder")

