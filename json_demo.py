import json
# json is a very common format for storing info. It stands for JavaScript Object Notation

people_string = '''
{
    "people": [
        {
            "name": "John Smith",
            "phone": "615-555-7164",
            "emails": ["johnsmith@bogusemail.com", "john.smith@work-place.com"],
            "has_license": false
        },
        {
            "name": "Jane Doe",
            "phone": "560-555-5153",
            "emails": null,
            "has_license": true
        }
    ]
}
'''

data = json.loads(people_string) # dictionary. See https://docs.python.org/3/library/json.html#encoders-and-decoders for conversions. Object -> dict, array -> list, string -> str, nul -> None, etc
print(type(data), data) # dict
print(type(data["people"]), data["people"]) # list

for person in data["people"]:
    print(type(person), person) # dict
    print(person["name"])
    
    del person["phone"]
    
new_string = json.dumps(data, indent=2, sort_keys=True) # JSON Python object -> JSON string. indent = 2 means for each level it indents it twice
print(type(new_string), new_string)

with open("states.json", "r") as f:
    data = json.load(f) # load from file. loads is from string
    
for state in data["states"]:
    print(state)
    del state["area_codes"]
    
    
with open("new_states.json", "w") as f:
    json.dump(data, f, indent=2) # dump converts to JSON file, dumps converts to string
    
    
# Yahoo Finance API example. Broken since Yahoo changed their API
from urllib.request import urlopen

with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
    source = response.read()

data = json.loads(source)

# print(json.dumps(data, indent=2))

usd_rates = dict()

for item in data['list']['resources']:
    name = item['resource']['fields']['name']
    price = item['resource']['fields']['price']
    usd_rates[name] = price

print(50 * float(usd_rates['USD/INR']))