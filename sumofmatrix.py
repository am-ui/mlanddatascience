def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print("\t", matrix[i][j], end=" ")
        print("\n")


def main():
    m = int(input("enter rows"));
    n = int(input("enter columns"));


    matrix1 = [[0 for j in range(0, n)] for i in range(0, m)]
    matrix2 = [[0 for j in range(0, n)] for i in range(0, m)]
    res_matrix = [[0 for j in range(0, n)] for i in range(0, m)]
    print("enter first matrix elements")
    for i in range(0, m):
        for j in range(0, n):
            matrix1[i][j] = int(input("enter an element"))
    print("enter second matrix elements ")
    for i in range(0, m):
        for j in range(0, n):
            matrix2[i][j] = int(input("enter an element"))

    for i in range(0, m):
        for j in range(0, n):
            res_matrix[i][j] = matrix1[i][j] + matrix2[i][j]

    print(" matrix 1")
    print_matrix(matrix1)
    print(" matrix 2")
    print_matrix(matrix2)


    print("resultant matrix after adding")
    print_matrix(res_matrix)


main()