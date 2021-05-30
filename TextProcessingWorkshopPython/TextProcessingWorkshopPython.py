from pyral import Rally, rallyWorkset

#read creads
params = []
with open(r'C:\Users\User\Desktop\!temp') as my_file:
    for line in my_file:
        params.append(line)

serverText = params[0].rstrip()
userText = params[1].rstrip()
passwordText = params[2].rstrip()
workspaceText = params[3].rstrip()
projectText = params[4].rstrip()
rootFolderText = params[5].rstrip() #TF15961 
queryText = params[6].rstrip()