import pymongo
import certifi


ca = certifi.where()
client = pymongo.MongoClient("mongodb+srv://usuario-pruebas:mWaa2bPv8vocwHM2@cluster0.mfkie5o.mongodb.net/?retryWrites=true&w=majority",tlsCAFile=ca)


db = client.test
print(db)


baseDatos = client["bd-registro-academico"]
print(baseDatos.list_collection_names())