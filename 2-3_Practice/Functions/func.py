#function
# def sqr(num):
#     return num ** 3

# result = sqr(5)
# print(result)

# parameter
# def add(n1, n2):
    # return n1 % n2

# print(add(1, 2))

#polymorphism
# def mult(p1, p2):
#     return p1 * p2

# print(mult('m', 2))
# print(mult(5, 'k'))

# import math

# def circle(rad):
#     ar =  math.pi * rad ** 2
#     circu = 2 * math.pi * rad
#     return ar, circu

# print(circle(5))

#lambda function
# cube = lambda x : x ** 3

# print(cube(2))

# multiple arguments
# def allsum(*args):
#     print(args)
#     return sum(args)

# print(allsum(1,8,9,8,7,9,8,2))

# #**kwargs multiple arguments
# def print_kwargs(**kwargs):
#     for key, value in kwargs.items():
#         print(key, value)
    
# print_kwargs(name="amit", power="none", skills="web dev")

#yield method
# def even_gen(limit):
#     for i in range(2, limit + 1, 2):
#         yield i
        
# for num in even_gen(12):
#     print(num)

# def fact(n):
#     if n == 0:
#         return 1
#     else :
#         return n * fact(n - 1)

# print(fact(5))