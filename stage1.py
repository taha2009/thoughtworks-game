import json
import requests

r = requests.get('https://http-hunt.thoughtworks-labs.net/challenge/input', headers={'userId':'mJd0SADp8'})
jsonInput = json.loads(r.text)

message = jsonInput['encryptedMessage']
key = jsonInput['key']

L = list(message)

alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
decrypted_word_list = []

for c in L:
	if c.capitalize() in alphabets:
		char_index = alphabets.index(c.capitalize()) + 1
		diff = char_index - key
		if diff > 0:
			decrypted_word_list.append(alphabets[diff - 1])
		else:
			diff = 26 + diff
			decrypted_word_list.append(alphabets[diff - 1])
	else:
		decrypted_word_list.append(c)

new_word = ''.join(decrypted_word_list)

new_word_list = {'message':new_word}
print(new_word_list)

r = requests.post('https://http-hunt.thoughtworks-labs.net/challenge/output', data=json.dumps(new_word_list), headers={'content-type': 'application/json','userId':'mJd0SADp8'})
print(r.text)
