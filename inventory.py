import json

initial=[
  {"title": "The Alchemist", "author": "Paulo Coelho", "price": 12.99, "in_stock": 'true'},
  {"title": "1984", "author": "George Orwell", "price": 9.99, "in_stock": 'true'}
]

with open("inventory.json","w")as file:
    json.dump(initial,file,indent=2)
    print("Total number of books:",len(initial))
    
new_book = {"title": "Atomic Habits", "author": "James Clear", "price": 14.99, "in_stock": True}

with open("inventory.json","r")as file:
    inventory=json.load(file)
inventory.append(new_book)

with open("inventory.json", "w") as file:
    json.dump(inventory, file, indent=4)

with open("inventory.json","r")as file:
    inventory=json.load(file)
    
    for book in inventory:
        print(f"Title: {book['title']} | Author: {book['author']} | Price: ${book['price']}")

   