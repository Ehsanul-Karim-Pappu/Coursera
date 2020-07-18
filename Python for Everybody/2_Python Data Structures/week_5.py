l = []
for line in open(input()):
    if line.startswith('From') and not line.startswith('From:'):
        l.append(line.split()[1])

unique = set(l)
counts = {}
for item in unique:
    counts[item] = l.count(item)
########
# counts = dict()
# for key in l:
#     if key in counts:
#         counts[key] = counts[key] + 1
#     else:
#         counts[key] = 1
########
# counts=dict()
# for word in l:
#     counts[word]=counts.get(word,0)+1
########
mx = 0
mx_mail = ''
for keys, values in counts.items():
    if mx < values:
        mx = values
        mx_mail = keys

print(mx_mail, mx)
