import requests

# Fetch data from the provided URL
def getUrlList(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        data = r.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return []

# Fetch data from the website
room_data_url = "http://sephbin.pythonanywhere.com/roomNames"
room_data = getUrlList(room_data_url)

# Collect unique values for class, department, and name
unique_classes = set()
unique_departments = set()
unique_names = set()

for room in room_data:
    unique_classes.add(room.get('class', 'N/A'))
    unique_departments.add(room.get('department', 'N/A'))
    unique_names.add(room.get('name', 'N/A'))

print("Unique Classes:")
for class_name in sorted(unique_classes):
    print(f"Class: {class_name}")
print()

print("Unique Departments:")
for department_name in sorted(unique_departments):
    print(f"Department: {department_name}")
print()

print("Unique Names:")
for room_name in sorted(unique_names):
    print(f"Name: {room_name}")
