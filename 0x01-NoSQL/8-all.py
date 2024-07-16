#!/usr/bin/env python3
"""
will List all documents in Python
"""


def list_all(mongo_collection):
    """
    will lists all documents in a collection

    :param mongo_collection:
    :return:
    """
    return mongo_collection.find()
