import json

# Opening JSON file
f = open('timetable.json', )
# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
for i in data:
    print(i, data[i])

# Closing file
f.close()