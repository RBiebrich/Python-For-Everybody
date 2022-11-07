name = input("Enter file: ")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
    if line.startswith("From "):
        words = line.split()
        emails = words[1]
        counts[emails] = counts.get(emails, 0) + 1
bigcount = None
bigemail = None
for emails, count in counts.items():
    if bigcount is None or count > bigcount:
        bigemail = emails
        bigcount = count

print (bigemail, bigcount)