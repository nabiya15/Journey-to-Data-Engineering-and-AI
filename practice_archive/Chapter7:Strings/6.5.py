text = "X-DSPAM-Confidence:    0.8475"
fpos= text.find(' ')
ntext= text[fpos:].strip()
print(float(ntext))