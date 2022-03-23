# questão 8.4 , letra b)
#considerando que uma imagem seja representada por uma matrix N x N de pixels, como explicitado no exercício

#functions
def read_matrix(R, C, mat):
	for i in range(R):         
	    a =[]
	    for j in range(C):      
	         a.append(int(input()))
	    matrix.append(a)
  
def print_matrix(R, C, mat):
	for i in range(R):
	    for j in range(C):
	        print(mat[i][j], end = " ")
	    print()


def tranpose_matrix(R, C, mat):
	for i in range(R):         
	    for j in range(i+1, C):
            	mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

def rotate_matrix_in_90degrees_clockwise(R, C, mat):

	tranpose_matrix(R, C, mat)
	
	size = C

	#reverse each row
	for i in range(R):         
	    for j in range(int(size/2)):
		    temp = mat[i][j]
		    mat[i][j] = mat[i][size-1-j]
		    mat[i][size-1-j] = temp

	
 #program 
# faço a chamada tanto de linhas quanto de colunas, mas apenas por formalidade

R = int(input("Enter the number of rows:\n"))
print(R)
print("\n")
C = int(input("Enter the number of columns:\n"))
print(C)
print("\n")
  
matrix = []
print("Enter the entries rowwise:")
read_matrix(R, C, matrix)

print_matrix(R, C, matrix)

print("\n")

rotate_matrix_in_90degrees_clockwise(R, C, matrix)

print_matrix(R, C, matrix)