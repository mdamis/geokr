import json

with open('geokr.json') as data_file:
    data = json.load(data_file)

photos = data["photos"]["photo"]
geotagged = []

print len(photos)

for photo in photos:
    if photo["longitude"] != 0 or photo["latitude"] != 0:
        print photo["longitude"]
        print photo["latitude"]
        geotagged.append(photo)

print(len(geotagged))

for photo in geotagged:
    print photo
