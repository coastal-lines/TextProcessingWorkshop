from bs4 import BeautifulSoup

text = '<p>Start to pass Test Form1 as Candidate1.<br/>Provide answers so that grade is failed. Finish Test. Check Test screen.</p>'
data = BeautifulSoup(text)
allBr = data.find("body").findAll("br")
for br in allBr:
    br.name = ""

t=0