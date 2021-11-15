def multiplication_table(size):
    size = size - 1
    A = [[None] * size for i in range(size)]
    for i in range(size):
        for j in range(size):
            A[i][j] = (i+1)*(j+1)
    return A


print(multiplication_table(5))
