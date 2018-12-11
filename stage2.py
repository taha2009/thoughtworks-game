import json
import requests

r = requests.get('https://http-hunt.thoughtworks-labs.net/challenge/input', headers={'userId':'mJd0SADp8'})
jsonInput = json.loads(r.text)

hiddenTools = jsonInput['hiddenTools']
hiddenToolsSet = list(hiddenTools) 
tools = jsonInput['tools']
final_tools = []

for tool in tools:
	found_tool = []
	tool_set = list(tool)
	init_index = 0
	for c in hiddenToolsSet:
		if c == tool_set[init_index]:
			found_tool.append(c)
			if len(tool) - 1 == init_index:
				break
			init_index+=1

	if tool == ''.join(found_tool):
		final_tools.append(tool) 


final_tool_list = {'toolsFound':final_tools}
print(final_tool_list)


r = requests.post('https://http-hunt.thoughtworks-labs.net/challenge/output', data=json.dumps(final_tool_list), headers={'content-type': 'application/json','userId':'mJd0SADp8'})
print(r.text)