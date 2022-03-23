
# questão 8.4 , letra a)
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
#turn upside down
def reverse_matrix(R, C, mat):
	l = int(R*C/2)
	k=0
	aux_mat = mat
	for i in range(R):
		for j in range(C):
			if k>l:
				break
			temp = mat[i][j]
			mat[i][j]=mat[R-1-i][C-1-j]
			mat[R-1-i][C-1-j]=temp
			k+= 1
		if k>l:
			break


		
		



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


reverse_matrix(R, C, matrix)

print_matrix(R, C, matrix)

print("\n")