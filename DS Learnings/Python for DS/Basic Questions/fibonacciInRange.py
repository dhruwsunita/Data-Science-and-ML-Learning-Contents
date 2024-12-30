# 1st method

# fib = [0,1]

# for i in range(5):
#     fib.append(fib[-1] + fib[-2])

# print(', '.join(str(e) for e in fib))


# Using recursion
# def fib(n):
#     if n <= 1:
#         return n
#     else:
#         return (fib(n-1) + fib(n-2))
    
# print(fib(8))


# Using Yeild

# def fib():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a+b

# f1 = fib()
# for _ in range(8):
#     print(next(f1))


# Optimization of Fibonacci

def fib(n):
    a = 0
    b = 1

    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return n
    elif n == 1:
        return n
    else:
        for i in range(1, n):
            c = a + b
            a = b 
            b = c
        return c

print(fib(5))