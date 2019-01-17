def maximum_boarder_length(w):
    n = len(w)
    L = [0] * (n+1)
    for i in range(1, n):
        k = L[i]
        while(w[k] != w[i] and k > 0):
            k = L[k]
        if w[k] == w[i]:
            L[i+1] = k+1
        else:
            L[i+1]=0
    return L


print(maximum_boarder_length('abaaba'))