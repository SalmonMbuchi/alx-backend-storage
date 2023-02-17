#!/usr/bin/env python3
"""Log stats"""
from pymongo import MongoClient


if __name__ == '__main__':
    """Provides stats about Nginx logs in MongoDB"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    # connect to logs database and nginx collection
    collection = client.logs.nginx
    # print(f'{collection.estimated_document_count()} logs')
    print(f'{collection.count_documents({})} logs')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    print('Methods:')
    for method in methods:
        count = collection.count_documents({'method': method})
        print(f'\tmethod {method}: {count}')
    statuscheck = collection.count_documents(
        {'method': 'GET', 'path': '/status'})
    print(f'{statuscheck} status check')
