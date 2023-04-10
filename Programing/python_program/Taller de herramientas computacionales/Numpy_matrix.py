import numpy as np

A = np.array([[1,2],[2,3]])
invA = np.linalg.inv(A)
detA = np.linalg.det(A)
eigenvalues,eigenvectors = np.linalg.eig(A)

print("A=\n{}".format(A))

print("---------------------")

print("inv(A)=\n{}".format(invA))

print("---------------------")

print("det(A)={}".format(detA))

print("---------------------")

print("eigenvalues(A)={}".format(eigenvalues))

print("---------------------")

print("eigenvectors(A)=\n{}".format(eigenvectors))
