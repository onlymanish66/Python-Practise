def Matrix_multiply():
    r1 ,c1 = map(int,input("Enter no. of rows and column for matrix A ").split())
    r2 ,c2 = map(int,input("Enter no. of rows and column for matrix B ").split())
    if r1 != c2:
        print("Miultiplication is not possible")
    else:
        print("Enter the elements in Matrix A ")
        A= [list(map(int,input().split())) for i in range(r1)]
        print("Enter the elements in Matrix B")
        B= [list(map(int,input().split())) for i in range(r2)]
        C = [[0]*c1 for i in range(r1)]
        for i in range(r1):
            for j in range(c2):
                for k in range(c1):
                    C[i][j] += A[i][k]*B[k][j]
    print("Result: ")
    for row in C:
        print(row)


Matrix_multiply()