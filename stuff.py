import pymongo
import json

connection = pymongo.MongoClient('homer.stuy.edu')
db = connection.cosh
collection = db.complaints

def setup():
    data = json.load(open("views.json"))
    collection.insert_many(data)

#setup()

def query_name(name):
    c = collection.find( { "name": name } )
    for x in c:
        print x
        #print "found " + name

def query_download_count(count):
    c = collection.find( {"downloadCount": count} )
    for x in c:
        print x
        #print "found " + str(count)
    
def query_owner(name):
    c = collection.find({ "owner.displayName": name })
    for x in c:
        print x
        #print "found " + name

def query_table_owner(name):
    c = collection.find({ "tableAuthor.displayName": name })
    for x in c:
        print x
        #print "found " + name

def query_tag(tag):
    c = collection.find({"tags": tag })
    for x in c:
        print x
        #print "found " + tag
    
query_name("Survey of Credit Card Plans")
query_download_count(1449)
query_owner("ming")
query_table_owner("Doug Taylor")
query_tag("credit cards")
