l = []
for line in open(input()):
    for word in line.split():
        l.append(word)

l = list(set(l))
l.sort()
print(l)
