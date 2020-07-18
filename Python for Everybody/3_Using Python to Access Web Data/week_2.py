import re

print(sum([int(i) for i in re.findall('[0-9]+', open("http://py4e-data.dr-chuck.net/regex_sum_770364.txt").read())]))
