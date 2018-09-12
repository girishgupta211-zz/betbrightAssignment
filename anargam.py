from collections import Counter


# Write a function that accepts a word (string) and
# a list of words (list or tuple of strings) and return
# back a list with the valid anagrams for the word
# inside the given words list.

def isAnagram(string1, string2):
    return Counter(string1) == Counter(string2) if len(string1) == len(
        string2) else False
    # builtin function Counter is better than sorted as it will
    # reduce complexity to O(n)
    # return sorted(string1) == sorted(string2)


def getAnagrams(word, words_list):
    """ Returns the list of valid anagrams for given word from
    input list/tuple of string"""
    # Remove spaces and convert to lower case
    try:
        return [each for each in words_list if
                isAnagram(each.replace(' ', '').lower(),
                          word.replace(' ', '').lower())]
    except AttributeError as ex:
        return "input data format is wrong"
