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
number = 5
fact = 1
while number > 0:
    fact = fact * number
    number = number - 1
    
print("Factorial", fact)