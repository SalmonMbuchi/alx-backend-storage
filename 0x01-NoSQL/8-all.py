#!/usr/bin/env python3
"""List all documents in a collection"""


def list_all(mongo_collection):
    """return empty list if no document in the collection"""
    myList = []
    for obj in mongo_collection.find():
        if obj is None:
            return []
        myList.append(obj)     
    return myList
