fname = input("Enter file name: ")
fhand = open(fname)
lst = list()
for line in fhand:
    line = line.rstrip()
    words = line.split()

    for i in words:
        if i not in lst:
            lst.append(i)
    lst.sort()
print(lst)