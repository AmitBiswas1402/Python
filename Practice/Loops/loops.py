# 1st 
# no = {9,-5,1,-5,4,-2}
# count = 0

# for i in no:
#     if i > 0:
#         count += 1
        
# print("Total No", count)
    
#2nd 
# no = {9,5,1,5,4,2}
# count = 0

# for i in no:
#     if i%2==0:
#         count += 1
        
# print("Total No", count)

#3rd
# n = 3

# for i in range(1, 11):
#     print(n, 'x', i, '=', n*i)

#4th Reverse a string
# str = "LEVEL"
# rev_str = ""

# for char in str:
#     rev_str = char + rev_str
    
# print(rev_str)

#5th non repeated charecter
# str = "twitter"
# for char in str:
#     print(char)
#     if str.count(char) == 1:
#         print("Char is: ", char)
#         break

#6th factorial
# number = 5
# fact = 1
# while number > 0:
#     fact = fact * number
#     number = number - 1
    
# print("Factorial", fact)

#7th
# while True:
#     number = int(input("Enter b/w 1 n 10: "))
#     if 1 <= number <= 10:
#         print("Thanks")
#         break
#     else:
#         print("Try again")

#8th Prime no
# n = 29
# prime = True
# if n > 1:
#     for i in range(2, n):
#         if(n % i) == 0:
#             prime = False
#             break
        
# print(prime)

#9th dupicate item in array
# items = ["a", "b", "a"]

# unique = set()

# for item in items:
#     if item in unique:
#         print("Duplicate: ", item)
#         break
#     unique.add(item)

#10th exponential backoff (wait time increment)
# import time
# wait = 1
# max_try = 5
# att = 0

# while att < max_try:
#     print("Attempt", att + 1, "wait time", wait)
#     time.sleep(wait)
#     wait *= 2
#     att += 1