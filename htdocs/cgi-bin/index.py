import datetime
from string import Template

nowDate = datetime.datetime.now().strftime('%Y年%m月%d日');
nowTime = datetime.datetime.now().strftime('%H:%M:%S');

file = open('./index.html', 'r', encoding="utf-8")
rowData = file.read()
data = Template(rowData)
file.close()

print('Content-type: text/html\n')
print(data.substitute(nowdate=nowDate, nowtime=nowTime))
