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

def zipgrade(db,zip,grade):
    output = db.restaurants.find({"address.zipcode" : zip, "grades.0.grade" : "A"})
    print "Testing the zip and grade"
    for restaurant in output:
        str1 = restaurant["name"]
        str2 = restaurant["address"]["zipcode"]
        str3 = restaurant["grades"][0]["grade"]
        print str1 + " is in the " + str2 + " and has a grade of " + str3
    print "Done testing zip and grade"
    print "-----------------------------------------------------------"

def zipthresh(db,zip,thresh):
    output = db.restaurants.find({"address.zipcode" : zip, "grades.0.score" : {"$lt" : thresh}})
    print "Testing the zip and threshold"
    for restaurant in output:
        str1 = restaurant["name"]
        str2 = restaurant["address"]["zipcode"]
        str3 = restaurant["grades"][0]["score"]
        print str1 + " is in the " + str2 + " and has a score of " + str(str3)
    print "Done testing zip and threshold...threshold was " + str(thresh)
    print "-----------------------------------------------------------"

def clever(db,zip,thresh,type):
        output = db.restaurants.find({ "$or" : [{"address.zipcode" : zip, "grades.0.score" : {"$gt" : thresh}},{"cuisine" : "type"}]})
        print "Testing the zip and threshold or type of cuisine"
        for restaurant in output:
            str1 = restaurant["name"]
            str2 = restaurant["address"]["zipcode"]
            str3 = restaurant["grades"][0]["score"]
            str4 = restaurant["cuisine"]
            print str1 + " is in the " + str2 + " and has a score of " + str(str3) + " and the cuisine was " + str4
        print "Done testing (clever) zip and threshold...threshold was " + str(thresh) + " or cuisine was " + type
        print "-----------------------------------------------------------"



def test():
    connection = MongoClient("homer.stuy.edu")
    db = connection.test
    borough(db,"Bronx")
    zipcode(db,"11209")
    zipgrade(db,"11209","A")
    zipthresh(db,"11209",5)
    clever(db,"11209",10,"Bakery")
    print "Done Testing...Wooooooooooooooooooooooooooooo"







test()
