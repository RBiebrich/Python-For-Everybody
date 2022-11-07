def computepay(h, r):
    if h > 40:
        ovr = r * 1.5 * (h - 40)
        pay = ovr + (r * 40)
    else:
        pay = h * r
    return pay

hrs = input("Enter Hours: ")
hrs = float (hrs)
rate = input ("Enter Rate: ")
rate = float (rate)

p = computepay (hrs, rate)
print("Pay", p)