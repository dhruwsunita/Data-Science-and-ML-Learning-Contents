a = '546'
print(int(a))

#  1 using split String to list
# str1 = "Sunita Dhruw"
# print(str1.split(" "))

# 2 using list keyword
# s = 'Sunita'
# l = list(s)
# print(l)


# 3 using list comprehension
# s = 'Sunita'
# l = [i for i in s]
# print(l)


# 4 using string slicing
# def Convert(string):
#     list1 = []
#     list1[:0] = string
#     return list1
# str1 = "Sunita"
# print(Convert(str1))


# 5 using enumerate function
# s = 'Sunita'
# l = [i for a, i in enumerate(s)]
# print(l)


# sort a python list
# list1 = [3,6,1,8]
# list1.sort()
# print(list1)


# delete a file in python 
# import os
# os.remove('delete.txt')


# list cocatenate
# l1 = [2, 5, 8, 6]
# l2 = [3,8,7,5]
# l3 = l1 + l2
# print(l1 + l2)

# lst1 = ['W', 'a', 'w', 'b']
# lst2 = ['e', ' ', 'riting', 'log']
# lst3 = [x + y for x, y in zip(lst1, lst2)]
# print(lst3)


# deleting a number from a list
# 1. By using remove()
# list1 = [2, 4, 6, 7]
# print(list1.remove(4))  # will printt None
# print(list1)

# By using pop()
# list2 =[4,7,8,9]
# print(list2.pop(2))
# print(list2)


# delete entire list
# list2 = [2, 6, 7, 9]
# list2.clear()   # list var still exist we can print it will give empty list []
# del list2      # gives an error if we want to print the list after delete operation


