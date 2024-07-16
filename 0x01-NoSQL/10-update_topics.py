#!/usr/bin/env python3
"""
this will Change school topics
"""


def update_topics(mongo_collection, name, topics):
    """
    this will changes all topics of a school
     document based on the name

    :param mongo_collection:
    :param name:
    :param topics:
    :return:
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
