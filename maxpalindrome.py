# Given a string *s*, find the longest palindromic substring in *s*.
#
# i.e. "book" should return "oo" or "abcdtacocatefghijk" should return "tacocat"
string = 'cookbaaaaaabcoockabcdtacocatefghijkbook'


def longest_palindrome(string):
    max_palindrome = ''

    for idx, letter in enumerate(string):
        i = 0
        while i < len(string):
            word = string[idx:idx + i]
            if word == word[::-1] and len(word) > len(max_palindrome):
                max_palindrome = word
            i += 1

    if len(max_palindrome) < 2:
        print("No palindrome found")
    else:
        print(f"max_palindrome: {max_palindrome}, length: {len(max_palindrome)}")


longest_palindrome(string)



# # !!!! Still not working completely !!!! Sometimes some weird substring appears

# def longest_palindrome(string):

#     max_palindrome = ''
#     print(f"Length of String: {len(string)}")

#     for idx, letter in enumerate(string):

#         if idx + 1 < len(string) and letter == string[idx + 1]:
#             # True if "OO"
#             current_palindrome = f"{letter}{string[idx + 1]}"
#             i = 1
#             while idx - i >= 0 and idx + i < len(string):
#                 if string[idx - i] == string[idx + i]:
#                     current_palindrome = f"{string[idx - i]}{current_palindrome}{string[idx + i]}"
#                     if len(current_palindrome) > len(max_palindrome):
#                         max_palindrome = current_palindrome
#                     i += 1
#                 elif len(current_palindrome) > len(max_palindrome):
#                     max_palindrome = current_palindrome
#                     i = idx + 1
#                 else:
#                     i = idx + 1


#         elif (idx + 2) < len(string):
#             # True if "OXO"
#             i = 1
#             while idx - i >= 0 and idx + 2 + i < len(string):
#                 if letter == string[idx + 2]:
#                     base_palindrome = f"{string[idx:idx+3]}"
#                     while idx - i >= 0 and idx + 2 + i < len(string):
#                         if string[idx - i] == string[idx + 2 + i]:
#                             current_palindrome = f"{string[idx -i]}{base_palindrome}{string[idx + 2 + i]}"
#                             base_palindrome = current_palindrome
#                             if len(current_palindrome) > len(max_palindrome):
#                                 max_palindrome = current_palindrome
#                         i += 1
#                 else:
#                     i = idx + 1


#     print(f"max palindrome {max_palindrome} length {len(max_palindrome)}")
#     return max_palindrome


# # longest_palindrome("cookbaaaaaabcoock")

# longest_palindrome("cookbaaaaaabcoockabcdtacocatefghijkbook")

