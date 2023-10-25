
# Input from the user
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Initialize two empty matrices
matrix1 = []
matrix2 = []

# Input from the user for the first matrix
print("Enter elements of the first matrix:")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix1.append(row)

# Input from the user for the second matrix
print("Enter elements of the second matrix:")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix2.append(row)

# Initialize a result matrix for the addition
result_matrix = []

# Perform matrix addition
for i in range(rows):
    result_row = []
    for j in range(cols):
        result_row.append(matrix1[i][j] + matrix2[i][j])
    result_matrix.append(result_row)

# Display the result matrix
print("Resultant Matrix (Sum of the two matrices):")
for i in range(rows):
    for j in range(cols):
        print(result_matrix[i][j], end=" ")
    print()
