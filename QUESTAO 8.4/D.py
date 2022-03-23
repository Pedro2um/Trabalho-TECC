"""
(d) Set each pixel value yi to be the average of the neighbors of pixel i in the original
    image. By neighbors, we mean the pixels immediately above and below, and immediately 
    to the left and right. The center pixel has 4 neighbors; corner pixels have 2 
    neighbors, and the remaining pixels have 3 neighbors.
"""

def avg_of_neighbors(mat):
    """
    Return matrix with elements set to the average of their neighbors.
    """
    avgmat = []

    for r in range(len(mat)):
        avgrow = []
        for c in range(len(mat[0])):
            sum, count = 0, 0

            if r > 0:
                sum += mat[r - 1][c]
                count += 1
            if r < len(mat) - 1:
                sum += mat[r + 1][c]
                count += 1
            if c > 0:
                sum += mat[r][c - 1]
                count += 1
            if c < len(mat[0]) - 1:
                sum += mat[r][c + 1]
                count += 1

            count = count if count != 0 else 1
            avgrow.append(sum / count)
        avgmat.append(avgrow)

    return avgmat
    

def print_matrix(matrix):
    for row in matrix:
        print(row)

m = [[1,4,7], [2,5,8], [3,6,9]]

print("Original Matrix:")
print_matrix(m)
print("Averaged Matrix:")
print_matrix(avg_of_neighbors(m))