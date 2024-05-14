#!/usr/bin/env python3
def schools_by_topic(mongo_collection, topic):
    """Return a list of schools with the specified topic."""
    query = {"topics": {"$regex": topic, "$options": "i"}}
    cursor = mongo_collection.find(query)
    schools = list(cursor)
    return schools
