import re, os, sys
from urllib.request import urlopen
from openpyxl import Workbook

# Get the HTML source code of the webpage
html = str(urlopen('http://www.airportcodes.org/#').read()).replace('<br />', '\n')

# On the HTML source code, find every IATA code
# between parentheses and get the name of the city
list = [i[:i.index(')')+1] for i in re.findall(".*\([A-Z]{3}\)", html)]

# Replace every \n with an empty character
for i in range(len(list)):
    list[i] = list[i].replace(r'\n', '')       
    
# TO ADJUST: Remove the part of HTML source code from some cities
for i in range(len(list)):
    # If it contains a close-tag character near the end...
    if '>' in list[i]:
        # ... remove it
        string = list[i]
        list[i] = string[string.rfind('>')+1:]

# Append everything on an Excel file, parsed with 2 columns...
wb = Workbook()
ws = wb.active
for i in list:
    nome = i[0:i.index('(')]
    codice = i[i.index('(')+1:len(i)-1]
    ws.append([nome, codice])
    
# ... and save it
wb.save("%s/airportcodes.xlsx" % os.getcwd());