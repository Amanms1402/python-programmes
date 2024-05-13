def matrix_multiply(A, B):
    if len(A[0]) != len(B):
        print("Cannot multiply matrices. Number of columns in A must equal number of rows in B.")
        return None

    result = [[0] * len(B[0]) for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result

# Example matrices
A = [[1, 2, 3],
     [4, 5, 6]]

B = [[7, 8],
     [9, 10],
     [11, 12]]

# Perform matrix multiplication
result = matrix_multiply(A, B)

# Display the result
if result:
    print("Result of matrix multiplication:")
    for row in result:
        print(row)
