hand = open('E:\Python\Learning\\Using_Python_to_Access_Web_Data\mbox-short.txt')

'''for line in hand :
    line = line.strip()
    if line.find('From:') >= 0: 
        print(line)
print('*'*30)'''

import re
count = 0
for line in hand :
    line = line.strip()
    if re.search('^X-\S*', line):
        count += 1
        print(line)
print(count)

# re.search là kiếm chữ cần tìm trong đoạn text trả về True or False