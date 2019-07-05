# encoding=utf-8
import requests
from lxml import etree
import codecs
import os
import csv


# 读取并保存url
def get_data(url):
    path = './data.html'
    if os.path.exists(path):
        # 读取文件
        f = codecs.open(path, 'r', 'gb2312')
        html_text = f.read()
        f.close()
    else:
        # 读取远程
        response = requests.get(url)
        response.encoding = 'utf-8'
        html_text = response.text
        # 保存本地
        f = codecs.open(path, 'w', 'utf-8')
        f.write(html_text)
        f.close()
    return html_text


html_txt = get_data('http://datachart.500.com/ssq/?expect=100')
html = etree.HTML(html_txt)
trs = html.xpath('.//tbody[@id="tdata"]//tr')
headers = ['lottery_id', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17',
           '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', 'r1', 'r2',
           'r3', 'r4', 'r5', 'r6', 'r7', 'r8', 'r9', 'r10', 'r11', 'r12', 'r13', 'r14', 'r15', 'r16', 'r17',
           'r18', 'r19', 'r20', 'r21', 'r22', 'r23', 'r24', 'r25', 'r26', 'r27', 'r28', 'r29', 'r30', 'r31', 'r32',
           'r33']
rows = []
createVar = locals()
for tr in trs:
    row = []
    result = []
    lottery_id = tr.xpath('./td[1]//text()')
    if len(lottery_id):
        lottery_id = lottery_id[0]
        row.append(lottery_id)
    else:
        continue
    listTemp = range(1, 34)
    for i, s in enumerate(listTemp):
        p = './td[' + str(i + 2) + ']//text()'
        createVar['num_' + str(i + 1)] = tr.xpath(p)[0]
        if createVar['num_' + str(i + 1)] == str(i + 1):
            createVar['num_' + str(i + 1)] = '1'
            result.append(1)
        else:
            result.append(0)
        row.append(createVar['num_' + str(i + 1)])
    rows.append(row + result)
print rows
with open('lottery.csv', 'wb')as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)
