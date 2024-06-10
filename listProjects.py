import json
import urllib3

# Set SonarQube URL here or get it safely from User
url = ""
apiSuffix = "/api/components/search_projects?ps=500&p=1"

rawData = urllib3.urlopen(url + apiSuffix)
parseData = rawData.read()
dictData = json.loads(parseData)
for i in range(100):
    print (dictData['components'][i]['name'])
