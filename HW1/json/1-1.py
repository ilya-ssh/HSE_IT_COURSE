import json
sample_data =  '''{
    "Title": "The Great Adventure",
    "Author": {
        "FirstName": "Jane",
        "LastName": "Doe"
    },
    "PublishedYear": 2021,
    "Genres": ["Adventure", "Fantasy", "Mystery"],
    "ISBN": "123-456-789",
    "AvailableCopies": 5,
    "BorrowedBy": [
        {"Name": "John Smith", "BorrowedDate": "2024-01-15"},
        {"Name": "Emily White", "BorrowedDate": "2024-02-05"}
    ],
    "LibraryLocation": {
        "Section": "Fiction",
        "ShelfNumber": 12,
        "Aisle": "B"
    },
    "IsAvailable": true
}''' #fake json generated by chatgpt


obj = json.loads(sample_data)
print(obj)
print("Book title: ",obj["Title"])
print("Author: ", obj["Author"]["FirstName"], obj["Author"]["LastName"])
print("Published Year: ", obj["PublishedYear"])
print("Genres: ", ", ".join(obj["Genres"]))
print("ISBN: ", obj["ISBN"])
print("Available Copies: ", obj["AvailableCopies"])
print("Currently Borrowed By:")
for borrower in obj["BorrowedBy"]:
    print(f"- {borrower['Name']} (Borrowed on: {borrower['BorrowedDate']})")
