import re
hand = open('E:\Python\Learning\\Using_Python_to_Access_Web_Data\Assignment.txt')
mylist = []
for line in hand:
    line = line.strip()
    if re.findall('([0-9]+)',line):
        for item in re.findall('([0-9]+)',line):
            item = int(item)
            mylist.append(item)
print('Sum all numbers:', sum(mylist))
