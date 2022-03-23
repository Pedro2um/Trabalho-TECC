"""
(c) Translate the image up by 1 pixel and to the right by 1 pixel. In the translated
    image, assign the value yi = 0 to the pixels in the first column and the last row.
"""

def translate_delta(mat, dx, dy):
    """
    Return matrix with elements translated by dx and dy, filling the would-be
    empty spaces with 0. I feel this method may not be the most efficient.
    """
    rows, cols = len(mat), len(mat[0])

    # Filter out simple deltas
    if (dx == 0 and dy == 0):
        return mat
    elif (abs(dx) >= rows or abs(dy) >= cols):
        return [[0 for col in mat[0]] for row in mat]
    
    dmat = [] 

    # Create new matrix translated by dx and dy
    for r in range(rows):
        drow = []
        for c in range(cols):
            if (r + dy in range(rows) and c - dx in range(cols)):
                drow.append(mat[r + dy][c - dx])
            else:
                drow.append(0)
        dmat.append(drow)

    return dmat

def print_matrix(matrix):
    for row in matrix:
        print(row)

m = [[1,4,7], [2,5,8], [3,6,9]]
dx = 1
dy = 1

print("Original Matrix:")
print_matrix(m)
print("Translated Matrix:")
print_matrix(translate_delta(m, dx, dy))