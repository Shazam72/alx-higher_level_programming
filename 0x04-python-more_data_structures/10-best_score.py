#!/usr/bin/python3
def best_score(a_dictionary):
    return_value = None
    try:
        sorted_scores = sorted(a_dictionary.items(),
                               key=lambda v: v[1],
                               reverse=True)
        return_value = sorted_scores[0][0]
    finally:
        return return_value
