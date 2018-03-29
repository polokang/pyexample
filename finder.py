__author__ = 'Administrator'

import requests
import re
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    flag = 0
    res = []
    is_get_data = 0
    def handle_starttag(self, tag, attrs):
        if tag == 'td':
            for attr in attrs:
                if re.match(r'trackListEven', attr[1]):
                    self.flag = 1

        # def handle_endtag(self, tag):
            # print("Encountered an end tag :", tag)

    def handle_data(self, data):
        if self.flag == 1:
            if data == '\xa0':
                print("-----")
            elif data == '\u3000':
                print("-----")
            elif data == '\fffd':
                print("-----")
            else:
                print("==>data  :", data)
                self.flag = 0


# parser.feed('<html><head><title>Test</title></head><body><h1>Parse me!</h1></body></html>')

codeList = ['SE0188195AU','SE0188196AU','SE0188197AU','SE0188198AU']

payload = {'w': 'starex', 'cno': codeList[3]}
r = requests.post('http://www.starex.com.au/cgi-bin/GInfo.dll?EmmisTrack', data=payload)
# r.encoding = 'gbk'
# r = r.content.decode(r.encoding)

if r.status_code == 200:
    parser = MyHTMLParser()
    parser.feed(r.text)

# content = re.findall(r'<td', r.text)
# print(r.text)

# print(content)