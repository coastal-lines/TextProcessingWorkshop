from pyral import Rally, rallyWorkset
from Rally.TestsAndFoldersActions import TestsAndFoldersActions
import pickle
from bs4 import BeautifulSoup
import re



#load input list
inputsList = []
with open(r'C:\Temp2\New folder\DataVisualizationAndStatisticsForRally\Draft\inputsList.data', 'w+b') as f:
    inputsList = pickle.load(f)


t = 0