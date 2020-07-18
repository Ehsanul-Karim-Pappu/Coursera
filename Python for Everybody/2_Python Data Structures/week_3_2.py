s = 0
c = 0
for line in open(input()):
    if line.startswith("X-DSPAM-Confidence:"):
        s += float(line.strip("X-DSPAM-Confidence:"))
        c += 1

print("Average spam confidence: %.12f" % (s / c))
