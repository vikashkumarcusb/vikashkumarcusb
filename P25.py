
# Input from the user
rows1 = int(input("Enter the number of rows for the first matrix: "))
cols1 = int(input("Enter the number of columns for the first matrix: "))
rows2 = int(input("Enter the number of rows for the second matrix: "))
cols2 = int(input("Enter the number of columns for the second matrix: "))

# Check if matrix multiplication is possible
if cols1 != rows2:
    print("Matrix multiplication is not possible. Columns of the first matrix must be equal to rows of the second matrix.")
else:
    # Initialize two empty matrices
    matrix1 = []
    matrix2 = []

    # Input from the user for the first matrix
    print("Enter elements of the first matrix:")
    for i in range(rows1):
        row = list(map(int, input().split()))
        matrix1.append(row)

    # Input from the user for the second matrix
    print("Enter elements of the second matrix:")
    for i in range(rows2):
        row = list(map(int, input().split()))
        matrix2.append(row)

    # Initialize a result matrix for the multiplication
    result_matrix = []

    # Perform matrix multiplication
    for i in range(rows1):
        result_row = []
        for j in range(cols2):
            product = 0
            for k in range(cols1):
                product += matrix1[i][k] * matrix2[k][j]
            result_row.append(product)
        result_matrix.append(result_row)

    # Display the result matrix
    print("Resultant Matrix (Product of the two matrices):")
    for i in range(rows1):
        for j in range(cols2):
            print(result_matrix[i][j], end=" ")
        print()
