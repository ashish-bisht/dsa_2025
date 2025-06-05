def rotate_matrix(matrix):
    # transpose karna hai

    for row in range(len(matrix)):
        for col in range(row, len(matrix[0])):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

    for row in range(len(matrix)):
        matrix[row].reverse()

    
    return matrix


print(rotate_matrix([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))