import os
listdir = os.listdir('img')
for item in listdir:
	os.rename('img/' + item, 'img/' + item.lower())
