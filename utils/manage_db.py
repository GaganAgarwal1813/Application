import pymongo
def store_in_db(id,name,desc):
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb://20.228.199.180:3000/"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = pymongo.MongoClient(CONNECTION_STRING)
    db = client["mydatabase"]
    collection = db['model_service']
    collection.insert_one({"model_id":id,"model_name":name,"description":desc})
    print("Model information stored successfully.")
    return

def show_db():
    CONNECTION_STRING = "mongodb://20.228.199.180:3000/"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = pymongo.MongoClient(CONNECTION_STRING)
    db = client["mydatabase"]
    collection = db['model_service']
    res=collection.find({})
    for r in res:
        print(r)
    return
# store_in_db(1,"model1","test Model")
show_db()