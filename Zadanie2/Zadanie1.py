rawData = open("SMSSpamCollection.tsv", encoding="utf-8").read()
rawData[0:20]

parsedData = rawData.replace('\t', '\n').split('\n')
parsedData[0:5]
labelList = parsedData[0::2]
textList = parsedData[1::2]
print(labelList[0:5])
print(textList[0:5])

print(len(labelList))
print(len(textList))
print(labelList[-5:])

import pandas as pd

fullCorpus = pd.DataFrame({
    "label" : labelList[0:-1],
    "text" : textList
    })

print(fullCorpus.head())
