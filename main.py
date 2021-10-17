import json

# Opening JSON file
f = open('timetable.json', )
# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
for i in data:
    print("{0:12}{1}".format(i, data[i]))

# Closing file
f.close()