file = open('youtube.txt', 'w')

try:
    file.write('code')
finally:
    file.close()
    
with open('youtube.txt', 'w') as file:
    file.write('python')