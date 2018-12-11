import json
import requests
from collections import OrderedDict

r = requests.get('https://http-hunt.thoughtworks-labs.net/challenge/input', headers={'userId': 'mJd0SADp8'})
jsonInput = json.loads(r.text)

tools = jsonInput['tools']
maximumWeight = jsonInput['maximumWeight']

tools_sorted = sorted(tools, key=lambda k: k['value'], reverse=True) 

totalWeight = 0
finalTools = []
for t in tools_sorted:
	if (t['weight'] + totalWeight) <= maximumWeight:
		finalTools.append(t['name'])
		totalWeight += t['weight']
	else:
		continue

final_tool_list = {'toolsToTakeSorted': finalTools}
print(final_tool_list)

r = requests.post('https://http-hunt.thoughtworks-labs.net/challenge/output', data=json.dumps(final_tool_list), headers={'content-type': 'application/json','userId':'mJd0SADp8'})
print(r.text)