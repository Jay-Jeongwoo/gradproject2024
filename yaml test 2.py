import yaml

# Original Python rules for comparison
rules = {
    "Hat": {
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
                "args": ["http://sephbin.pythonanywhere.com/roomNames"]
            }
        }
    },
    "wall": {
        "fireRating": ["-", "120/120/120", "240/240/240"],
        "uniclassSSGroup": [[20, "Structural Systems"], [25, "Wall and barrier systems"]],
        "wall[uniclassSSGroup=25]": {
            "uniclassSSSubGroup": [
                [10, "Framed wall systems"],
                [11, "Monolithic wall structure systems"],
                [12, "Panel wall structure systems"]
            ]
        }
    },
    "wall[typeName*=\"Blockwork\"]": {
        "uniclassSSGroup": 25,
        "uniclassSSSubGroup": 11,
        "uniclassSSObject": 16,
        "uniclassSSObjectTitle": "Concrete wall systems"
    },
    "door[feature=\"Dropbolt\"]": {
        "fireEgressDoor": False
    }
}

# YAML data as a string
yaml_data = """
Hat:
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
        - http://sephbin.pythonanywhere.com/roomNames

wall:
  fireRating:
    - "-"
    - "120/120/120"
    - "240/240/240"
  uniclassSSGroup:
    - [20, "Structural Systems"]
    - [25, "Wall and barrier systems"]

wall[uniclassSSGroup=25]:
  uniclassSSSubGroup:
    - [10, "Framed wall systems"]
    - [11, "Monolithic wall structure systems"]
    - [12, "Panel wall structure systems"]

wall[typeName*="Blockwork"]:
  uniclassSSGroup: 25
  uniclassSSSubGroup: 11
  uniclassSSObject: 16
  uniclassSSObjectTitle: Concrete wall systems

door[feature="Dropbolt"]:
  fireEgressDoor: False
"""

loaded_rules = yaml.safe_load(yaml_data)

print("Loaded YAML Data:\n", loaded_rules)

print("Original Python Rules:\n", rules)

# Compare loaded YAML data with original Python dictionary
comparison_result = loaded_rules == rules
print("Comparison Result:", comparison_result)

# Detailed comparison
for key in rules.keys():
    if key in loaded_rules:
        print(f"\nComparing section: {key}")
        print(f"Original: {rules[key]}")
        print(f"Loaded: {loaded_rules[key]}")
        print(f"Match: {rules[key] == loaded_rules[key]}")
    else:
        print(f"Key {key} missing in loaded rules.")
