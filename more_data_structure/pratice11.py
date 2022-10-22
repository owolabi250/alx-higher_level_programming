#!/usr/bin/python3
def best_score(a_dictionary):
    new = 0
    if a_dictionary:
        for i in a_dictionary:
            if a_dictionary[i] > new:
                new = a_dictionary[i]
                n = i
        return n


a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))