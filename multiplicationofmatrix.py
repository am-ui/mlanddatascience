def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j],end=" ")
        print("/n")
def main():
    m=int(input("Enter the number of rows"))
    n=int(input("Enter the number of columns"))
    matrix1=[[0 for j in range(0,n)]for i in range(0,m)]
    matrix2=[[0 for j in range(0,n)] for i in range(0,m)]
    res_matrix=[[0 for j in range(0,n)] for i in range(0,m)]
    print(" Enter the elements of matrix")
    for i  in range(0,m):
        for j in range(0,n):
            matrix1[i][j]=int(input("enter the elements"))


    print("Enter the element of second matrix")
    for i in range (0,m):
        for j in range (0,n):
            matrix2[i][j]=int(input("Enter the elements"))

    print("resultant matrix is:")
    for i in range(0,m):
        for j in range(0,n):
            res_matrix[i][j]=matrix1[i][j]*matrix2[i][j]

    print(" matrix 1")
    print_matrix(matrix1)
    print(" matrix 2")
    print_matrix(matrix2)

    print("resultant matrix after multiplying")
    print_matrix(res_matrix)

main()
