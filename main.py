#mongodb+srv://<username>:<password>@krabaton.5mlpr.gcp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority

#python -m pip install "pymongo[srv]"==3.11



from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://goitlearn:<rizun2024>@cluster0.klgot1w.mongodb.net/nnij_bd?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)