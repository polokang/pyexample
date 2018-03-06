import requests

payload = {'w': 'starex', 'cno': 'SE0148049AU'}
	
r = requests.post('http://www.starex.com.au/cgi-bin/GInfo.dll?EmmisTrack',data=payload)

print(r.text)