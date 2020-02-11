import pymongo, csv
from pymongo import MongoClient
'''
path = "master.csv"
file = open(path, newline='')

for line in file:
	print(line)
'''
post = {"accountcode": "", "src": "", "dst": "", "dcontext": "", "clid": "", "channel": "", "dstchannel": "", "lastapp": "", "calldate": "" }
post.append({"answerdate": "", "hangupdate": "", "duration": "", "billsec": "", "disposition": "", "amaflags": "", "uniqueid": "", "userfield": ""})

print(post)

#cluster = MongoClient("mongodb+srv://dbadmin:Jackoff2019@cluster0-blkbq.gcp.mongodb.net/test?retryWrites=true&w=majority")

#db = cluster["issabel0718"]
#collection = db["usuarios"]

#post = {"nome": "Fabio", "sobrenome": "Salesse", "Celular": "4499423161"}
#collection.insert_one(post)