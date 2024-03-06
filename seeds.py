import json
from models2 import Author, Quote
import connect2

def load_authors():
    with open("authors.json", 'r', encoding="utf-8") as file:
        data_of_authors = json.load(file)
        for author in data_of_authors:
            auth = Author(fullname=author.get("fullname"),
                         born_date=author.get("born_date"),
                         born_location=author.get("born_location"),
                         description=author.get("description"))
            auth .save()
    with open("qoutes.json", 'r', encoding="utf-8") as file:
        data_of_quotes = json.load(file)
        for quote_ in data_of_quotes:
            quot = Quote(author_id=quote_.get("author_id"),
                         quote=quote_.get("quote"),
                         tags=quote_.get("tags"))
            quot.save()    
            
if __name__ == '__main__':        
    load_authors()
