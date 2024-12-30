# vowels = ['a','e','i','o','u']
# word = 'sunita dhruw'
# count = 0
# for ch in word:
#     if ch in vowels:
#         count += 1

# print(count)


# counting consonants
# vowels = ['a','e','i','o','u']
# word = 'programming'
# count = 0
# for ch in word:
#     if ch not in vowels:
#         count += 1

# print(count)


# Using dictionary
# word = "Programming Language"
# vowels = 'aeiouAEIOU'
# ch = {}

# for i in word:
#     if i in vowels:
#         if i in ch:
#             ch[i] += 1
#         else:
#             ch[i] = 1

# print(ch)

# Using regex

# import re

# def count_vowels(string):
#     vowels = '[aeiouAEIOU]'
#     count = len(re.findall(vowels, string))
#     return count

# string = "Hello world"
# print(count_vowels(string))


# Using count method
def count_vowels(string):
  vowels = 'aeiouAEIOU'
  count = 0
  for vowel in vowels:
    count += string.count(vowel)
  return count

# Example usage:
string = 'Hello, world!'
print(count_vowels(string))



   


