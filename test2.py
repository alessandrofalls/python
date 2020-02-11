import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://dbadmin:Jackoff2019@cluster0-blkbq.gcp.mongodb.net/test?retryWrites=true&w=majority")

db = cluster["issabel0718"]
collection = db["usuarios"]

post = {"nome": "Fabio", "sobrenome": "Salesse", "Celular": "4499423161"}
collection.insert_one(post)