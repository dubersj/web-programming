# Creating a Mongita database with movie info
import json
from mongita import MongitaClientDisk

quotes = [
    {"text":"I'm hungry. When's lunch?","author":"Dorothy"},
    {"text":"I'm thirsty. Glub glub","author":"Angelfish"}
]

# Writing the data to a Mongita DB file

# create Mongita client connection
client = MongitaClientDisk()

# create movie database
quotes_db = client.quotes_db

# create a sci fi collection
quotes_collection = quotes_db.quotes_collection

#sci_fi_collection.count_documents({})

# put quotes in database
quotes_collection.insert_many(quotes)

# makes sure quotes are there
print(quotes_collection.count_documents({}))