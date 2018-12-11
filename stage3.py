import json
import requests
import datetime
from collections import OrderedDict

r = requests.get('https://http-hunt.thoughtworks-labs.net/challenge/input', headers={'userId':'mJd0SADp8'})
jsonInput = json.loads(r.text)

toolUsage = jsonInput['toolUsage']
tool_usage_duration = {}

for t in toolUsage:
	diff = datetime.datetime.strptime(t['useEndTime'], '%Y-%m-%d %H:%M:%S') - datetime.datetime.strptime(t['useStartTime'], '%Y-%m-%d %H:%M:%S')
	diff_minutes = int(diff.seconds / 60)
	tool_usage_duration[t['name']] = tool_usage_duration.get(t['name'], 0) + diff_minutes

tool_usage_final = []
for tool, duration in tool_usage_duration.items():
	tool_usage_final.append({'name' : tool, 'timeUsedInMinutes': duration})

d_descending = sorted(tool_usage_final, key=lambda k: k['timeUsedInMinutes'], reverse=True) 

final_tool_duration_list = {'toolsSortedOnUsage':d_descending}
print(final_tool_duration_list)

r = requests.post('https://http-hunt.thoughtworks-labs.net/challenge/output', data=json.dumps(final_tool_duration_list), headers={'content-type': 'application/json','userId':'mJd0SADp8'})
print(r.text)