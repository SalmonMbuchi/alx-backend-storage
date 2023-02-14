#!/usr/bin/env python3
"""Where can I learn Python?"""


def schools_by_topic(mongo_collection, topic):
    """Returns the list of school with a topic"""
    aList = []
    aList.append(mongo_collection.find({"topics": topic}))
    return aList
