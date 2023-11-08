from pymongo import MongoClient

uri = "mongodb+srv://googlecalendarcluster.9ttbu0x.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
certificate_path = "resources_package_mongodb/certificate_test_user.pem"
database_name = "calendar"
collection_name = "eventsToday"


def private_get_eventsToday_collection():
    try:
        # Connect to MongoDB using the provided URI and certificate
        client = MongoClient(uri, tls=True, tlsCertificateKeyFile=certificate_path)
        
        # Access the specified database and collection
        db = client[database_name]
        collection = db[collection_name]
        return collection
    
    except Exception as e:
        print("An error occurred:", e)

def insert_events_to_mongodb(data_list):
    collection = private_get_eventsToday_collection()
    result = collection.insert_many(data_list)
        
    print("Inserted", len(result.inserted_ids), "documents into", collection_name)
    
def retrieve_events_from_mongodb():
    collection = private_get_eventsToday_collection()
    events = list(collection.find({}))
    return events
        