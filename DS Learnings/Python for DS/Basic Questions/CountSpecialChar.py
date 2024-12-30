import re

string = "Sunit%is&a*gi@lan#sh!"

count = re.sub("[\w]+", "", string)

print(len(count))