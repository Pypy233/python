from urllib.request import urlopen
import json
import ssl
context = ssl._create_unverified_context()
def getCountry(idAddress):
	response = urlopen('http://freegeoip.net/json/' + idAddress, context = context).read().decode('utf-8')
	responseJson = json.loads(response)
	return responseJson.get('country_code')


print(getCountry('52.78.253.58'))