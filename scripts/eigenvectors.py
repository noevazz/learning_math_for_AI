import torch

A = torch.tensor([[25., 2., 9.], [5., 26., -5.], [3., 7., -1.]])

print("A matrix:")
print(A)

eValues, eVectors = torch.linalg.eig(A)
eValues = eValues.float()
eVectors = eVectors.float()

print("Eigen values:", eValues)
print("Eigen vectors:\n", eVectors)

print()
print("Check if Av=λv")

print("Av=", torch.matmul(A, eVectors[:,0]))
print("λv=", eValues[0]*eVectors[:,0])