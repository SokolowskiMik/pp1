import json

fav = {
    "title": "A Brief History of Time",
    "Author": {"Name": "Stephen", "Surname": "Hawking"},
    "Publication": 1988,
    "Pages": 256,
    "Topic": "theoretical cosmology"
}

with open("08-DictionariesStacksAndQueues\\favourite.json", "w") as file:
    f = file

