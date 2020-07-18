def computepay(h, r):
    if a[0] > 40:
        a[0] = (40 * a[1] + (a[0] - 40) * a[1] * 1.5)
    else:
        a[0] = (a[0] * a[1])
    return a[0]


a = list(map(float, input().split()))
p = computepay(a[0], a[1])
print("Pay", p)
