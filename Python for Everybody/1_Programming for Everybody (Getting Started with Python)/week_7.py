lst = []
while True:
    t = input()
    try:
        a = int(t)
        lst.append(a)
    except:
        if t == "done":
            print("Maximum is", max(lst))
            print("Minimum is", min(lst))
            break
        else:
            print("Invalid input")
