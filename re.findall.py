import re
hand = open('E:\Python\Learning\\Using_Python_to_Access_Web_Data\mbox-short.txt')

x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('@([^ ]+)', x)
print(y)
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)
for line in hand:
    line = line.strip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)',line)
    if len(stuff) !=1 :continue
    print(re.findall('^X-DSPAM-Confidence: [0-9.]+',line))
