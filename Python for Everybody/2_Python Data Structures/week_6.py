# l = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# for line in open(input()):
#     if line.startswith('From') and not line.startswith('From:'):
#         l[int(line.split()[5].split(":")[0])] += 1

# i = 0
# for l[i] in l:
#     if l[i]:
#         if i < 10:
#             print('0' + str(i), l[i])
#         else:
#             print(i, l[i])
#     i += 1
##############################################################################

l = {}
for line in open(input()):
    if line.startswith('From') and not line.startswith('From:'):
        l[line.split()[5].split(":")[0]] = l.get(
            line.split()[5].split(":")[0], 0) + 1

hr = []
for keys in l:
    hr.append(int(keys))

hr.sort()
for i in hr:
    if i < 10:
        print('0' + str(i), l['0' + str(i)])
    else:
        print(i, l[str(i)])
