#!/usr/bin/env python3
"""Log stats"""
from pymongo import MongoClient


if __name__ == '__main__':
    """Provides stats about Nginx logs in MongoDB"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    # connect to logs database and nginx collection
    collection = client.logs.nginx
    print(f'{collection.estimated_document_count()} logs')
    get = collection.count_documents({'method': 'GET'})
    post = collection.count_documents({'method': 'POST'})
    put = collection.count_documents({'method': 'PUT'})
    patch = collection.count_documents({'method': 'PATCH'})
    delete = collection.count_documents({'method': 'DELETE'})
    statuscheck = collection.count_documents(
        {'method': 'GET', 'path': '/status'})
    print(f'Methods:\n\tmethod GET: {get}\n\
        method POST: {post}\n\tmethod PUT: {put}\n\
        method PATCH: {patch}\n\tmethod DELETE: {delete}')
    print(f'{statuscheck} status check')
