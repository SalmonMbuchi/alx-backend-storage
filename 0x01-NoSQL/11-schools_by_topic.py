#!/usr/bin/env python3
"""Where can I learn Python?"""


def schools_by_topic(mongo_collection, topic):
    """Returns the list of school with a topic"""
    aList = []
    for school in mongo_collection.find({"topics": topic}):
        aList.append(school)
    return aList
