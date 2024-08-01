import requests
import yaml
from pydantic import BaseModel, ValidationError, Field, field_validator
from typing import List, Dict, Any

# To fetch data from the URL
def getUrlList(url: str) -> List[Dict[str, Any]]:
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return []

# Load the rules from the YAML file
with open("rules.yaml", "r") as file:
    rules = yaml.safe_load(file)
    print("Loaded Rules:")
    print(rules)

# Fetch data from the URL
room_data_url = rules['room']['name']['choices']['args'][0]
room_data = getUrlList(room_data_url)
valid_room_names = [room['name'] for room in room_data]
print("Valid Room Names:")
print(valid_room_names)

# Dynamic Pydantic model for validation
class RoomModel(BaseModel):
    name: str

    @field_validator('name')
    def name_must_be_in_choices(cls, value):
        if value not in valid_room_names:
            raise ValueError(f"Invalid room name: {value}. Must be one of {valid_room_names}")
        return value

# Validate fetched room data against the rules
for room in room_data:
    try:
        validated_room = RoomModel(**room)
        print(f"Validated Room: {validated_room}")
    except ValidationError as e:
        print(f"Validation error for room {room['name']}: {e}")
