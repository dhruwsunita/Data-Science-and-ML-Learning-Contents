#  1st Method
# def reverse_string(s):
#     rev_str = ""
#     for i in range(len(s)-1, -1, -1):
#         rev_str += s[i]
#     return rev_str


# s = "Sunita dhruw"
# print(reverse_string(s))


# 2nd Using slicing method
# def reverse_string(s):
#     return s[::-1]
# print(reverse_string('Sunita'))


# Using reverse keyword
# def reverse_string(s):
#     rev_str = "".join(reversed(s))
#     return rev_str

# print(reverse_string("Sunita"))

# Using recursion
# def reverse_string(string):
#     if len(string) == 0:
#         return string
#     else:
#         return reverse_string(string[1:]) + string[0]


# string = "hello world"
# reversed_string = reverse_string(string)
# print(reversed_string)


#  Using List Comprehension
# def reverse_string(s):
#     reversed_string = [s[i] for i in range(len(s)-1, -1, -1)]
#     return "".join(reversed_string)

# s = "Sunita Dhruw"
# print(reverse_string(s))



# Reverse a string
# str1 = "Sunita Dhruw"
# str2 = ""

# for i in str1:
#     str2 = i + str2
# print(str2)


# def isPalindrome(self, x: int) -> bool:
#     if x < 0:
#         return False

#     reversed_num = 0
#     temp = x

#     while temp != 0:
#         digit = temp % 10
#         reversed_num = reversed_num * 10 + digit
#         temp //= 10

#     return reversed_num == x