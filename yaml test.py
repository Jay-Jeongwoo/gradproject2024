import yaml

# Original Python rules for comparison
rules = {
    "True": {
        "choiceTest": {"enum": ["apple", "banana", 55]},
        "arrayTest": {
            "maxItems": 3,
            "minItems": 3,
            "prefixItems": [{"type": "integer"}, {"type": "string"}, {"type": "string"}],
            "type": "array"
        }
    },
    "room": {
        "name": {
            "choices": {
                "func": "getUrlList",
                "args": ["https://dummyjson.com/test/"]
            }
        }
    },
    "wall": {
        "fireRating": ["-", "120/120/120", "240/240/240"],
        "uniclassSSGroup": [(20, "Structural Systems"), (25, "Wall and barrier systems")],
        "wall[uniclassSSGroup=25]": {
            "uniclassSSSubGroup": [
                (10, "Framed wall systems"),
                (11, "Monolithic wall structure systems"),
                (12, "Panel wall structure systems")
            ]
        }
    }
}

# YAML data as a string
yaml_data = """
True:
  choiceTest:
    enum:
      - apple
      - banana
      - 55
  arrayTest:
    maxItems: 3
    minItems: 3
    prefixItems:
      - type: integer
      - type: string
      - type: string
    type: array

room:
  name:
    choices:
      func: getUrlList
      args:
        - https://dummyjson.com/test/

wall:
  fireRating:
    - "-"
    - "120/120/120"
    - "240/240/240"
  uniclassSSGroup:
    - [20, Structural Systems]
    - [25, Wall and barrier systems]

wall[uniclassSSGroup=25]:
  uniclassSSSubGroup:
    - [10, Framed wall systems]
    - [11, Monolithic wall structure systems]
    - [12, Panel wall structure systems]

wall[typeName*="Blockwork"]:
  uniclassSSGroup: 25
  uniclassSSSubGroup: 11
  uniclassSSObject: 16
  uniclassSSObjectTitle: Concrete wall systems

door[feature="Dropbolt"]:
  fireEgressDoor: False
"""

# Load YAML data
loaded_rules = yaml.safe_load(yaml_data)

# Print the loaded YAML data to see what it looks like as a Python dictionary
print("Loaded YAML Data:\n", loaded_rules)

# Print the original rules for comparison
print("Original Python Rules:\n", rules)

# Compare loaded YAML data with original Python dictionary
comparison_result = loaded_rules == rules
print("Comparison Result:", comparison_result)  # This should print True if the conversion is correct

