import requests
import yaml

# Fetch data from the provided URL
def getUrlList(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        data = r.json()
        return list(data)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return []

# Load the rules from the YAML file
with open("roomrules.yaml", "r") as file:
    rules = yaml.safe_load(file)
    print("Loaded Rules:")
    print(rules)

# Process the rules
for selector, properties in rules.items():
    if selector:
        for k, v in properties.items():
            print(f"\nProcessing: {k}")
            if isinstance(v, dict):
                for varArgKeyword, varArgValue in v.items():
                    if isinstance(varArgValue, dict) and "func" in varArgValue:
                        dynamicFunction = globals().get(varArgValue["func"])
                        if dynamicFunction:
                            args = varArgValue.get("args", [])
                            result = dynamicFunction(*args)
                            print(f"Result from {varArgValue['func']}: {result}")
                        else:
                            print(f"Function {varArgValue['func']} not found.")
            elif isinstance(v, list):
                print(f"List value for {k}: {v}")
            else:
                print(f"Unexpected type for {k}: {type(v)}")

print(data)
