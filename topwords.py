# Return word from list that are repeated the most, the argument k represent the top k word repeated in the list.

# Example:
# Input: words = ["i","love","sun", "i","love","pizza"], k = 2
# Output: ["i","love"]

# @param String[] $words
# @param Integer $k
# @return String[]
# 

def top_frequent_words(words, k):
    dict_word = {} # empty dictionary to store the string word and amount of time they appear
    for word in words: # check if key in dictionary
        if word in dict_word:
            dict_word[word] += 1  # Add +1 to the key value
        else:
            dict_word[word] = 1 # create new value

            # dict_word looks like:  { abc: 1, cde: 3, fgt:1}
    return_string = []  # initiate return string
    while k > 0:  # use k provided to get the to repetition and create boundaries to the loop
        max_word = ''
        max_value = max(dict_word.values())  # find max value eg.. 1,2,3,4 that a word is repeated in the list
        keys = []  # initiate a list to store key that have the same value
        for key, value in dict_word.items():
            if max_value == value:
                keys.append(key) # Add all the key with the max value to the list
        keys.sort()  # sort by alphab order
        max_word = keys[0]  # get the first word from that ordered list

        return_string.append(max_word) # Add key to the list we are going to return
        del dict_word[max_word]  # remove key/value from dictionary
        k -= 1  # decrease k to avoid looping through all the dictionary value

    print(return_string)  # to confirm

    return return_string

#  Test:
top_frequent_words(["i", "love", "something", "i", "love", "sun", "sea"], 4)
