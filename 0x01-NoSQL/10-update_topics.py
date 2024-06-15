#!/usr/bin/env python3
""" MongoDB Operations  """


def update_topics(mongo_collection, name, topics):
    """ Changes topics of school doc """
    query = {"name": name}
    new_values = {"$set": {"topics": topics}}

    mongo_collection.update_many(query, new_values)
