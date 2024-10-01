import json
sample_data = {
    "Title": "The Great Adventure",
    "PublishedYear": 2021,
    "Genres": ["Adventure", "Fantasy", "Mystery"],
    "ISBN": "123-456-789",
    "AvailableCopies": 5,
    "IsAvailable": True}


json_data = json.dumps(sample_data, indent=4, sort_keys=True)
print(json_data)
