lst = ['P','Y','T','H','O','N']
# lst.append(['g','k'])
# print(lst)   # it will add like ['P','Y','T','H','O','N',['g','k']]
# lst.extend(['a','o'])
# print(lst)  # o/p => ['P', 'Y', 'T', 'H', 'O', 'N', ['g', 'k'], 'a', 'o']

#  1. Method using join
# string =""
# print(string.join(lst))
# print(type(string))


# 2. Method using for loop
# def listToStr(lst):
#     str1 = ""
#     for ele in lst:
#         str1 += ele
#     return str1 
# lst = ['Sunita','is' ,'a','girl']
# print(listToStr(lst))


# 3 Method using list comprehension

# lstToStr = ''.join([str(item) for item in lst])
# print(lstToStr)


# 4 Method using map function
# lstToStr = ''.join(map(str, lst))
# print(lstToStr)

# 5 using format
# result = "{}{}{}{}{}{}".format(*lst)
# print(result)

# 6 using recursion
def list_str(start, l, word):
    if(start == len(l)):
        return word
    
    word += str(l[start])+' '

    return list_str(start+1, l, word)

l = ['Sunita','is' ,'a','girl']
print(list_str(0, l, ''))