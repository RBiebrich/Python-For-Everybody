name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()
hours = list ()
for line in handle:
    if line.startswith("From "):
        words = line.split()
        times = words[5]
        time = times.split(":")
        hours.append(time[0])

hours = sorted(hours)

for hour in hours:
    counts[hour]=counts.get(hour, 0)+1

for key, val in counts.items():
    print (key, val)