import requests
import yaml
from pydantic import BaseModel, ValidationError, model_validator
from typing import List, Dict, Any

# Function to fetch data from URL
def getUrlList(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        data = r.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return []

# Load rules from YAML file
with open("rules.yaml", "r") as file:
    rules = yaml.safe_load(file)
    print("Loaded Rules:")
    print(rules)

# Fetch data from the website
room_data_url = rules['room']['name']['choices']['args'][0]
room_data = getUrlList(room_data_url)
valid_room_names = [room['name'] for room in room_data]
print("Valid Room Names:")
print(valid_room_names)

# Define dynamic Pydantic model for validation
class RoomModel(BaseModel):
    name: str

    @model_validator(mode='before')
    def check_name(cls, values):
        name = values.get('name')

        # Validate name
        if not isinstance(name, str):
            raise ValueError(f"Name must be a string: {name}")
        if len(name.split()) > rules['room']['name']['max_words']:
            raise ValueError(f"Name '{name}' exceeds maximum of {rules['room']['name']['max_words']} words")
        if name not in valid_room_names:
            raise ValueError(f"Invalid room name: {name}. Must be one of {valid_room_names}")

        return values

# Collect errors
errors = []

# Validate room names
for room in room_data:
    try:
        validated_room = RoomModel(name=room['name'])
        print(f"Validated Room: {validated_room}")
    except ValidationError as e:
        errors.append((room, e.errors()))

# Display errors
if errors:
    print("\nValidation Errors:")
    for room, error_list in errors:
        print(f"\nRoom: {room}")
        for err in error_list:
            field = err.get('loc', ['unknown'])[0] if isinstance(err.get('loc'), list) else 'unknown'
            print(f"  Field: {field}, Error: {err['msg']}")



