c = 0
for line in open(input()):
    if line.startswith('From') and not line.startswith('From:'):
        print(line.split()[1])
        c += 1

print("There were %d lines in the file with From as the first word" % c)
