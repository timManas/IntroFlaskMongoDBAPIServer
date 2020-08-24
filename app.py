#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from flask import Flask
from flask import Flask
from flask_pymongo import pymongo




app = Flask(__name__)
@app.route('/')
def flask_mongodb_atlas():
    return "flask mongodb atlas!"


@app.route("/test")
def test():

    CONNECTION_STRING = "mongodb+srv://timmanas:Apple@cluster0-9czdc.mongodb.net/flask_mongodb_atlas?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"
    client = pymongo.MongoClient(CONNECTION_STRING)

    db = client.get_database('flask_mongodb_atlas')

    # Print Sample table
    SampleTable = db.SampleTable
    print ("SampleTable:", SampleTable)

    # Insert One Ex1
    user_collection = pymongo.collection.Collection(db, 'user_collection')
    db.db.collection.insert_one({"name": "John"})


    # Insert One  Ex2
    db = client['flask_mongodb_atlas']
    collection = db['SampleCollection']

    # Change this
    document = {"company": "Quincy Inc",
                "city": "Toronto",
                "country": "US"}

    id = collection.insert_one(document).inserted_id
    print("id: ", id)



    return "Connected to the data base!"


if __name__ == '__main__':
    app.run(port=8000)



'''
How to Run

0. Go to file and execute using this command:
python3 app.py

1. Go to browser and type in
localhost:8000
localhost:8000/test

2. Go to mongodb atlas and see the newly created entries are there

'''