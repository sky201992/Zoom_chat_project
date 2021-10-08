import pandas as pd
#To read the file
file = open(r'08102021.txt','r') 
#reading file line by line
linedata = file.readlines()
lst = [] #to store final dictonery to create DataFrame
lst1 = [] #to store multiple line text
for j,i in enumerate(linedata):
    if i[0] == 'F':
        dict1 = {} #for creating DataFrame
        lst1 = [] #here we reset list
        fr = i.find('From') #it will store starting location of From
        To = i.find('to') #it will store starting location of to
        msgto = i.find(':') #it will store starting location of :
        msgtype = i.find('(') #it will store starting location of (
        msgtype1 = i.find(')') #it will store starting location of )
        dict1['From'] = i[fr+5:To]
        dict1['To'] = i[To+3:msgto]
        dict1['MessageType'] = i[msgtype+1:msgtype1]
        dict1['MessageTime'] = i[msgtype1+1:-1]
    else:
        txt = ""
        i = i.strip("\n") #removing \n(new line)
        lst1.append(i)
        for i in lst1:
            txt = txt +" "+ i
        dict1['Text'] = txt
        if j == len(linedata)-1 or linedata[j+1][0] == 'F':
            lst.append(dict1)
df = pd.DataFrame(lst)
df.to_excel('ZoomChat.xlsx','sheet1')



