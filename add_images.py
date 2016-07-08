#!/usr/bin/python

import fileinput
import json

lineBuffer = []
for line in fileinput.input():
    lineBuffer.append(line)

rawJson = "".join(lineBuffer)
parsedJson = json.loads(rawJson)
shinchosha = parsedJson["book_groups"]["shinchosha"]

folderToPublisherMap = {
    "Shinchosha" : ["shinchosha", ""],
    "Kadokawa": ["kadokawaShoten", "k"],
    "English": ["kondanshaEnglish", "e"],
    "Comics": ["comicBooks", "cm"],
    "Korean": ["korean", "chishiki"],
    "Rironsha": ["rironsha", "r"]

}

for folderName, bookDataKey in folderToPublisherMap.items():
    books = parsedJson["book_groups"][bookDataKey[0]]["books"]

    i = 0
    for book in books:
        i = i + 1
        book["img"] = "/assets/books/" + folderName + "/" + bookDataKey[1] + str(i) + ".jpg"

    parsedJson["book_groups"][bookDataKey[0]]["books"] = books

print json.dumps(parsedJson, indent=4, separators=(',', ': '))
