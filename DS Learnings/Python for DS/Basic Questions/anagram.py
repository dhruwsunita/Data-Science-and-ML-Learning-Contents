# Using list and sort method

# str1 = 'Listen'
# str2 = 'Silent'

# str1 = list(str.upper(str1))
# str2 = list(str.upper(str2))
# str1.sort()
# str2.sort()

# if str1 == str2:
#     print("Anagram")
# else:
#     print("Not an anagram")


# Using sorted method

# def are_anagrams(str1, str2):
#     return sorted(str.lower(str1)) == sorted(str.lower(str2))

# if are_anagrams("Silent", "Listen"):
#     print("Strings are anagrams")
# else:
#     print("Strings are not anagrams")


#  Using Counter

from collections import Counter

def are_anagrams(str1, str2):
    return Counter(str.lower(str1)) == Counter(str.lower(str2))

if are_anagrams("Silent", "Listen"):
    print("Strings are anagrams")
else:
    print("Strings are not anagrams")

