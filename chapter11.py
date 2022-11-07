import re

name = input("Enter file: ")
if len(name) < 1:
    name = "regex_sum_data.txt"
fhand = open(name)
data = fhand.read()
nums = re.findall('[0-9]+', data)
tot = 0
for i in nums:
    i = int(i)
    tot = tot + i
print (tot)