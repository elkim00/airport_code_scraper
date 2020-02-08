import requests
from urllib.request import urlopen
import re

html = str(urlopen('http://www.airportcodes.org/#').read()).replace('<br />', '\n')
list = [i[2:i.index(')')+1] for i in re.findall(".*\([A-Z]{3}\)", str(html))]
print (list)
print (len(list))

file = open("C:\\Users\\S22178\\Desktop\\airportcodes.txt", "w")
for i in list: file.write(i + '\n')
file.close();