#!/usr/bin/env python3
"""this adds accpoording to kwargs"""
from pymongo import mongo_client


def insert_school(mongo_collection, **kwargs):
    """this add in in a collectiom"""
    if kwargs:
        result = mongo_collection.insert_one(kwargs)
        return result.inserted_id
