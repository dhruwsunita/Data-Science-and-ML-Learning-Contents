# Using map
# lst = [1,2,3,4,5]

# m = list(map(lambda x: x*x, lst))
# print(m)


# filter using 
numbers = (2, 15, 24, 8, 12)

f = tuple(filter(lambda x:(x%3 == 0), numbers))

print(f)

# square of each number using loop
l1 = [8, 5, 7, 9]
l2 = []
for i in l1:
    l2.append(i*i)
print(l2)