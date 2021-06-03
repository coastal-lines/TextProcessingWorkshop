from bs4 import BeautifulSoup

text = '<span style="background-color:#ffffff; font-family:NotoSans,Helvetica,Arial; line-height:17.1429px">Check Media file on the&nbsp;</span><u style="background-color:#ffffff; box-sizing:border-box; font-family:NotoSans,Helvetica,Arial; line-height:17.1429px">Introduction page.</u>'
data = BeautifulSoup(text)
sp = data.find_all("u")

textList = []
for li in liList:
    span = li.find_all("span")
    if (span[0].text != ""):
        textList.append(li.getText())
        continue
    textList.append(li.text)
t=0

    position = -1
    for line in listInputs:
        position = position + 1

        if(line == '\xa0'):
            listInputs.pop(position)

        if('\n' in line):
            line = " ".join(line.splitlines())
            listInputs[position] = line

        tempLine = line.strip()
        if(len(tempLine) == 0):
            listInputs.pop(position)