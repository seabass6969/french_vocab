import json
import csv
topic_name = input("Give me the topic name: ")
fileopen = open("result.json","a")
with open("./frenchenglish.csv", 'r') as file:
  csvreader = csv.reader(file, delimiter=';')
  for row in csvreader:
    french = row[0]
    english = row[1]
    jsonoutput = {"french": "{}".format(french), "english": "{}".format(english), "topic_name": "{}".format(topic_name), "foundation": True, "higher": True, "theme_based": True, "theme": "Current and future study and employment"}
    outputString = json.dumps(jsonoutput)
    fileopen.write(outputString)
    fileopen.write(",")
    fileopen.write('\n')


fileopen.close()