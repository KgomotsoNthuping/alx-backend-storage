#!/usr/bin/env python3
""" MongoDB Operations """


def list_all(mongo_collection):
    """ List all docs """
    documents = mongo_collection.find()

    if documents.count() == 0:
        return []

    return documents
