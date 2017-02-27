import json
import requests
import sys
import urllib2


money = raw_input("Dwste sunallagmata me keno: (px. EUR USD)\n")
money = money.split(" ")
print money
date = raw_input("Dwste hmeromhnia me morfh YYYY-MM-DD: \n")
print date

sunallagma = []
bitcoins = []
for i in range(len(money)):
	response = urllib2.urlopen("http://api.coindesk.com/v1/bpi/historical/close.json?start=%s&end=%s&currency=%s"%(date,date,money[i]))
	data = response.read()		
	json_data = json.loads(data)
	data = data.split(':')
	x= data[2].split("}")[0]
	print "H timh se "+money[i]+" tou bitcoin einai: "+x

	bitcoins.append(money[i])
	bitcoins.append(x)

print bitcoins
