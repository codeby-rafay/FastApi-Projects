from pymongo import MongoClient

MONGO_URI = "mongodb+srv://rafayali_21:rafayali210203@rafay-cluster.uazpuov.mongodb.net/?retryWrites=true&w=majority&tlsAllowInvalidCertificates=true"

try:
    conn = MongoClient(MONGO_URI, serverSelectionTimeoutMS=10000)
    # Test the connection
    conn.admin.command('ping')
except Exception as e:
    print(f"MongoDB connection error: {e}")
    conn = None
