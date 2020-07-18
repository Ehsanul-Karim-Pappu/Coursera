score = float(input())
if score >= .9:
    print("A")
elif score >= .8:
    print("B")
elif score >= .7:
    print("C")
elif score >= .6:
    print("D")
elif score < .6:
    print("F")
elif score < 0 and score > 1:
    print("Score must be between 0.0 t0 1.0")
