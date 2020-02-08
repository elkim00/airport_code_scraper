from urllib.request import urlopen
from openpyxl import Workbook
import re

html = '\n' + str(urlopen('http://www.airportcodes.org/#').read()).replace('<br />', '\n')
list = [i[ : i.index(')')+1 ] for i in re.findall(".*\([A-Z]{3}\)", str(html))]

for i in range(0, len(list)):
    if '\\n' in list[i]:
        list[i] = list[i][list[i].rfind('\\n')+2:]

wb = Workbook()
ws = wb.active
for i in list:
    nome = i[0:i.index('(')]
    codice = i[i.index('(')+1:len(i)-1]
    ws.append([nome, codice])
wb.save("C:\\Users\\S22178\\Desktop\\airportcodes.xlsx")
