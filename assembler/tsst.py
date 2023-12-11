def complement16(num):
    hexnum = [*num]
    for i in range(len(hexnum)):
        hexnum[i] = hex(15 - int(hexnum[i], 16))[2:]
    # str = "".join(hexnum)
    return hex((int("".join(hexnum), 16)) + 1)[2:]


print(complement16("e1"))
