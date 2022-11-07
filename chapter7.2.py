fname = input("Enter file name: ")
fhand = open(fname)
count = 0
tot = 0
for line in fhand:
    if not line.startswith("X-DSPAM-Confidence: "):
        continue
    count = count + 1
    pos = line.find('.')
    str = line[pos-1:pos+5]
    str = str.strip()
    value = float(str)
    tot = tot + value
avg = tot/count
print('Average spam confidence:', avg)