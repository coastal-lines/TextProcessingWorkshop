from pyral import Rally, rallyWorkset
from Rally.TestsAndFoldersActions import TestsAndFoldersActions
import pickle

#load input list
inputsList = None
with open(r'C:\Temp2\New folder\DataVisualizationAndStatisticsForRally\Draft\inputsList.data', 'rb') as f:
    inputsList = pickle.load(f)


t = 0