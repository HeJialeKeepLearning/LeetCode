def multiply(A):
    b = list(A)
    b[0] = 1
    for i in range(1, len(A)):
        b[i] = b[i - 1] * A[i - 1]
    temp = A[len(A) - 1]
    for i in range(len(b) - 2, -1, -1):
        b[i] *= temp
        temp *= A[i]
    return b

multiply([1, 2, 3, 4, 5])
