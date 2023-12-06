#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    maxscore = 0
    maxkey = None
    for k, s in a_dictionary.items():
        if s > maxscore:
            maxscore = s
            maxkey = k
    return maxkey
