from pymongo import MongoClient
#sudo pip install pymongo


def borough(db,place):
    output = db.restaurants.find({"borough" : place})
    print "Testing the Bronx"
    for restaurant in output:
        str1 = restaurant["name"]
        str2 = restaurant["borough"]
        print str1 + " is in the " + str2
    print "Done testing borough"
    print "-----------------------------------------------------------"

def zipcode(db,zip):
    output = db.restaurants.find({"address.zipcode" : zip})
    print "Testing the zipcode"
    for restaurant in output:
        str1 = restaurant["name"]
        str2 = restaurant["address"]["zipcode"]
        print str1 + " is in the " + str2
    print "Done testing zipcode"
    print "-----------------------------------------------------------"
#    db.restaurants.find({"address.zipcode" : "11209"}).pretty()




def test():
    connection = MongoClient("homer.stuy.edu")
    db = connection.test
    borough(db,"Bronx")
    zipcode(db,"11209")






test()
