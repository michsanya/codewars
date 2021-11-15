def alphabet_war(fight):
    fight = "_" + fight + "_"
    f = list(fight)
    g = list(fight)
    for i in range(len(f)):
        if f[i] == "*":
            g[i-1] = g[i] = g[i+1] = "_"
    fight = str(g)
    power = 0
    p = 0
    for char in fight:
        if char == "w":
            p = -4
        if char == "p":
            p = -3
        if char == "b":
            p = -2
        if char == "s":
            p = -1
        if char == "m":
            p = 4
        if char == "q":
            p = 3
        if char == "d":
            p = 2
        if char == "z":
            p = 1
        power = p + power
        p=0
    if power > 0:
        return "Right side wins!"
    if power < 0:
        return "Left side wins!"
    if power == 0:
        return "Let's fight again!"


print(alphabet_war("mb**qwwp**dm"))