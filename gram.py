import numpy as np


def gram_schmidt(matrix, num_of_row, num_of_col):
    U = np.copy(matrix)
    V = [] # buffer
    Q = np.zeros((num_of_row, num_of_col)) 
    
    rank = np.linalg.matrix_rank(U)
    
    if(rank == num_of_col):

        for i in range(num_of_col):
            v = np.copy(U[:, i]).reshape(matrix.shape[0],1) # initialize v_1, v_2, ...
            for j in range(0, i):
            	v = v - (np.inner(np.transpose(V[j]), np.transpose(v))/np.linalg.norm(V[j])**2) * V[j]
            V.append(v)

        for k in range(num_of_col):
                Q[:,k] = (V[k]/np.linalg.norm(V[k])).reshape(1,matrix.shape[0])

        return Q
    else:
        return ("The vectors are not linearly independant")
    
matrix=np.array([[1,2,1],[1,2,3],[2,4,2],[1,2,3]])

print(gram_schmidt(matrix,matrix.shape[0],matrix.shape[1]))
