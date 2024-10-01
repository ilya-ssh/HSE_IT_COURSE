import json
sample_data =  {
    "Title": "The Great Adventure",
    "PublishedYear": 2021,
    "Genres": ["Adventure", "Fantasy", "Mystery"],
    "ISBN": "123-456-789",
    "AvailableCopies": 5,
    "IsAvailable": True}
jsond = json.dumps(sample_data)
print(jsond)

