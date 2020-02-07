# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 07:25:27 2020

@author: Rag
"""
from pymongo import MongoClient

def connect():
    client = MongoClient('mongodb+srv://root:root@cluster0-6qril.mongodb.net/test?retryWrites=true&w=majority')
    db = client.get_database('rag')
    records = db.get_collection('votingsystem')
    return records

def insert(voter):
    records = connect()
    records.insert_one(voter)
    
voter = {
    'voterid' : '',
    'name' : '',
    'aadhar' : 0,
    'email-id': 0,
    'isVoted' : False,
    'isVerified': False
}
