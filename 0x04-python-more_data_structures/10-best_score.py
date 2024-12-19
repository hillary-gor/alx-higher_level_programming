#!/usr/bin/python3
#a function that returns a key with the biggest integer value
def best_score(my_dict):
    if my_dict is None or my_dict == {}:
        return None
    biggest = max(my_dict.values())
    for key, value in my_dict.items():
        if value is biggest:
            return key
