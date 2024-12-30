# string = "S un i ta "
# print(string.strip())


# remove space between letters
# my_string = " Hello World !"
# my_string_no_spaces = my_string.replace(" ", "")
# print(my_string_no_spaces)


# my_string = " Hello World !"
# my_string_no_spaces = " ".join(my_string.split())
# print(my_string_no_spaces)

# Remove whitespace from the beginning of a string
# string = "    This is a string with whitespace    ."
# string = string.lstrip()
# print(string)

# Remove whitespace from the end of a string
# string = "    This is a string with whitespace.    "
# string = string.rstrip()
# print(string)

# Use a regular expression to remove all whitespace
import re
string = "    This is a string with whitespace.    "
string = re.sub("\s", "", string)
print(string)
