from bs4 import BeautifulSoup

text = '<li class="rally-rte-class-08688b1e92a91">Go to&nbsp;<span class="rally-rte-class-0cba33f787a396">Surpass Editions</span>&nbsp;&gt; Home &gt;Deliver Test &gt; HTML Delivery &gt; Select<span class="rally-rte-class-0cba33f787a396">&nbsp;English&nbsp;</span>language</li>'
data = BeautifulSoup(text)
liList = data.find_all("li")

textList = []
for li in liList:
    span = li.find_all("span")
    if (span[0].text != ""):
        textList.append(li.getText())
        continue
    textList.append(li.text)
t=0



#create list of all Inputs
#remove html tags from inputs
inputsList = []
for tc in allTestCasesForSaveIntoFile:
    for input in tc.inputs:
        listOfInputsInsideOneStep = htmlParser(input)
        inputsList.extend(listOfInputsInsideOneStep)


saveLikeAText(inputsList)

#save input list into file
#with open(r'C:\Temp2\New folder\DataVisualizationAndStatisticsForRally\Draft\inputsList.data', 'w+b') as file:
 #   pickle.dump(inputsList, file)

#72 lines should be