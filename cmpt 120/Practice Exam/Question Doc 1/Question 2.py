def occur():

    s1 = input()
    s2 = input()
    counter = 0
    idx = 0


    while True:
        idx = s1.find(s2, idx)
        if idx >= 0:
            counter += 1
            idx += 1
        else:
            break
    print(counter)

occur()