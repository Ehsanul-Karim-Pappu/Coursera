a = list(map(float, input().split()))

if a[0] > 40:
    a[0] = (40 * a[1] + (a[0] - 40) * a[1] * 1.5)
else:
    a[0] = (a[0] * a[1])

print(a[0])
