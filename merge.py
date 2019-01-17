def merge(x, y):
    z = []
    i = 0
    j = 0
    while i< len(x) and j < len(y):
        if x[i] <= y[j]:
            z.append(x[i])
            i += 1
        else:
            z.append(y[j])
            j += 1

    if i == len(x)-1 and j == len(y) -1:
        return z

    if i == len(x) - 1:
        z = z + y[j:]
    else:
        z = z + x[i:]
    return z


def merge2(x, y):
    z = []
    i = 0
    j = 0
    while i < len(x) or j < len(y):
        if j == len(y) or (i < len(x) and x[i]<y[j]):
            z.append(x[i])
            i += 1
        else:
            z.append(y[j])
            j += 1
    return z




x = [1,2,3,4,5]
y = [3,4,7]

print(merge2(x, y))