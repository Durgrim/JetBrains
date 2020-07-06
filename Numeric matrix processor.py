def first_matrix():
    A_dim = [int(i) for i in input('Enter size of first matrix:').split()]
    A =[]
    print('Enter first matrix:')
    for i in range(A_dim[0]):
        A.append([float(j) for j in input().split()])
    return A

def single_matrix():
    A_dim = [int(i) for i in input('Enter size of matrix:').split()]
    A =[]
    print('Enter matrix:')
    for i in range(A_dim[0]):
        A.append([float(j) for j in input().split()])
    return A
    
def second_matrix():
    B_dim = [int(i) for i in input('Enter size of second matrix:').split()]
    B = []
    print('Enter second matrix:')
    for i in range(B_dim[0]):
        B.append([float(j) for j in input().split()])
    return B
        
def matrix_addition(matrix_1, matrix_2):
    matrix_sum = []
    if len(matrix_1) != len(matrix_2):
        print('The operation cannot be performed')
    else:
        for i in range(len(matrix_1)):
            matrix_sum.append([(matrix_1[i][j] + matrix_2[i][j]) for j in range(len(matrix_1[0]))])
        return matrix_sum
            
def matrix_mult(matrix_1, k):
    matrix_mult = []
    for i in range(len(matrix_1)):
        matrix_mult.append([round(matrix_1[i][j] * k, 3) for j in range(len(matrix_1[0]))])
    return matrix_mult

def transpose_main(matrix):
    for row in matrix: 
        transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))] 
    return transpose
    
def transpose_side(matrix):
    transpose = transpose_main(transpose_vertical(transpose_horizontal(matrix))) 
    return transpose

def transpose_vertical(matrix):
    transpose = [line[::-1] for line in matrix]
    return transpose

def transpose_horizontal(matrix):
    transpose = transpose_main(transpose_vertical(transpose_main(matrix)))
    return transpose
    
def matrix_dotproduct(matrix_1, matrix_2):
    if len(matrix_1[0]) != len(matrix_2): 
        print('The operation cannot be performed')
    else:
        dot_matrix = []
        matrix_2 = transpose_main(matrix_2)
        for i in range(len(matrix_1)):
            dot_smatrix = []
            for j in range(len(matrix_2)):
                result = 0
                for k in range(len(matrix_2[0])):
                    result += matrix_1[i][k] * matrix_2[j][k]
                dot_smatrix.append(result)
            dot_matrix.append(dot_smatrix)
        return dot_matrix

def minor(matrix, i, j):
    return [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]
    
def cofactor(i, j):
    return (-1) ** (i + j)

def matrix_cofactor(matrix):
    cof_matrix = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[0])):
            row.append(cofactor(i, j) * matrix_determinant(minor(matrix, i, j)))
        cof_matrix.append(row)
    return cof_matrix

def matrix_determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]

    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    determinant = 0
    for c in range(len(matrix)):
        determinant += ((-1)**c)*matrix[0][c]*matrix_determinant(minor(matrix,0,c))
    return determinant            

def matrix_inverse(matrix):
    inverse = (1 / matrix_determinant(matrix))
    if inverse == 0 or len(matrix) != len(matrix[0]):
        print("This matrix doesn't have an inverse.")
    else:
        return matrix_mult(transpose_main(matrix_cofactor(matrix)), inverse)
        

while True:
    print('\n1. Add matrices')
    print('2. Multiply matrix by a constant')
    print('3. Multiply matrices')
    print('4. Transpose matrix')
    print('5. Calculate a determinant')
    print('6. Inverse matrix')
    print('0. Exit')
    choice = int(input('Your choice: '))
    if choice == 1:
        A, B = first_matrix(), second_matrix()
        print('The result is: ')
        summatrix = matrix_addition(A, B)
        for line in summatrix:
            print(*line)
    elif choice == 2:
        A = single_matrix()
        C = int(input('Enter constant: '))
        print('The result is: ')
        multmatrix = matrix_mult(A, C)
        for line in multmatrix:
            print(*line)
    elif choice == 3:
        A, B = first_matrix(), second_matrix()
        print('The result is: ')
        dotmatrix = matrix_dotproduct(A, B)
        for line in dotmatrix:
            print(*line)
    elif choice == 4:
        print()
        print('1. Main diagonal')
        print('2. Side diagonal')
        print('3. Vertical line')
        print('4. Horizontal line')
        choice_2 = int(input('Your choice: '))
        if choice_2 == 1:
            A = single_matrix()
            At = transpose_main(A)
            for line in At:
                print(*line)
        elif choice_2 == 2:
            A = single_matrix()
            At = transpose_side(A)
            for line in At:
                print(*line)
        elif choice_2 == 3:
            A = single_matrix()
            At = transpose_vertical(A)
            for line in At:
                print(*line)
        elif choice_2 == 4:
            A = single_matrix()
            At = transpose_horizontal(A)
            for line in At:
                print(*line)     
    elif choice == 5:
        A = single_matrix()
        print('The result is:')
        print(matrix_determinant(A))
    elif choice == 6:
        A = single_matrix()
        print('The result is:')
        Ainverse = matrix_inverse(A)
        for line in Ainverse:
            print(*line)
    elif choice == 0:
        print('Goodbye!')
        break
