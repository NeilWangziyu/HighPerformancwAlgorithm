def levenshtein(x,y):
    # 编辑距离
    n = len(x)
    m = len(y)

    A = [[i+j for j in range(m+1)] for i in range(n+1)]

    for i in range(n):
        for j in range(m):
            A[i+1][j+1] = min(A[i][j+1]+1, A[i+1][j]+1, A[i][j] + int(x[i]!=y[j]))
    # print(A)
    return A[n][m]

if __name__ == "__main__":
    X = "aodi"
    Y = "aody"
    print(levenshtein(X, Y))


    X = "harrypotter"
    Y = "harryporrer"
    print(levenshtein(X, Y))