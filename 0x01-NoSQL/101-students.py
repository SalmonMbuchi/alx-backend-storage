#!/usr/bin/env python3
"""Top students"""


def top_students(mongo_collection):
    """returns all students sorted by average"""
    total_avg = {}
    for student in mongo_collection.find():
        average = student.topics.score / 3
        total_avg["averageScore"] = average
    total_avg = {key: val for key, val in sorted(total_avg.items())}
    return total_avg
