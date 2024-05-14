#!/usr/bin/env python3
"""this is for the pymongo"""
from pymongo import mongo_client


def list_all(mongo_collection):
    """this functioomreturn a list of collections"""
    docs = mongo_collection.find()
    
    if docs:
        return [doc for doc in docs]
    else:
        return []
