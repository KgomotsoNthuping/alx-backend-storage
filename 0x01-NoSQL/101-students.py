#!/usr/bin/env python3
""" MongoDB Operations """


def top_students(mongo_collection):
    # sourcery skip: inline-immediately-returned-variable
    """ Prints all students in a collection sorted by average score"""
    top_student = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])

    return top_student
