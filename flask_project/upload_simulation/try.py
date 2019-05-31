import sys,re,string
import pandas as pd
import csv
punclist = list(string.punctuation)
punclist.remove('#')
punclist.remove('@')

temp = []
temp.append(" @fictillius @christiansarkis @AndrewConstance ...")
temp.append(" Hey @AndrewConstance, thanks in advance for br...")
temp.append("@chris)(*&^s #SydneyTrains")
temp.append("State Election: Transport Minister @AndrewCons...")
temp.append("The worst delay was 21 minutes, on the 15:50 C...Between 16:00 and 18:30 today, 22% of trips ex...@Qantas is the #sydneytrains of the sky.The worst delay was 14 minutes, on the 08:17 C...")
mod_text = []
for line in temp:
    for char in punclist:
        line = line.translate(str.maketrans('','',char))
    mod_text.append(line)
print(mod_text)

dataframe = pd.DataFrame({'full_text':mod_text})
dataframe.to_csv("mod_text.csv",index = False,header=False)
#
# file = open('mod_text.csv','w')
# writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
#
# for line in mod_text:
# 	writer.writerows(mod_text)
