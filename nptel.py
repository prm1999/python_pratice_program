print(5)


def mystery(l):
    if l == []:
        return (l)
    else:
        return (mystery(l[1:]) + l[:1])


print(mystery([22, 14, 19, 65, 82, 55]))
