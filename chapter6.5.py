text = "X-DSPAM-Confidence:    0.8475"
npos = text.find("0")
num = text[npos:npos+6]
print (float(num))
