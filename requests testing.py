import requests
import yaml


with open("roomrules.yaml","r") as file:
	rules = yaml.safe_load(file)
	print(rules)


def getUrlList(url):
	r = requests.get("https://dummyjson.com/test")
	data = r.json()
	return list(data)

for selector, properties in rules.items():
	if selector:
		for k,v in properties.items():
			print(k,v)
			for varArgKeyword, varArgValue in v.items():
				if "func" in varArgValue:
					dynamicFunction = globals()[varArgValue["func"]]
					result = dynamicFunction(*varArgValue["args"])
					print(result)


#print(data)