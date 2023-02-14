#!/usr/bin/env python3
"""Insert a document in a collection"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """insert a documnet based on kwargs"""
    result = mongo_collection.insert_one(**kwargs)
    return result.inserted_id
