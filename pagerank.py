#!/usr/bin/env python
import numpy as np

filename = "network.txt"
N = 5

A = np.zeros((N, N))

for line in open(filename):
    node_i, node_j = line.strip().split()

    node_i = int(node_i)
    node_j = int(node_j)

    A[node_i, node_j] = 1

print("Original network")
print(A)

def Google_Matrix(A, m):
    N = A.shape[0]
    v = np.ones(N)

    KT = np.dot(A, v)
    A = A.T

    for i in range(N):
        if KT[i] != 0:
            A.T[i] = A.T[i]/KT[i]
        else:
            A.T[i] = np.ones(N)/float(N)

    S = np.ones((N, N))/N
    G = (1-m)*A+m*S

    return G

def Power_Method(G, n_iter):
    N = G.shape[0]
    x0 = np.ones(N)/N

    print(0, x0, np.sum(x0))

    for i in range(n_iter):
        x1 = np.copy(x0)
        x0 = np.dot(G, x0)
        print(i+1, x0, np.sum(x0))
        if np.sum(np.abs(x1-x0)) < 1e-10:
            break

    return x0

m = 0.15
n_iter = 100

# Question 5
G = Google_Matrix(A, m)

print("\nGoogle Matrix")
print(G)

print("\nPower method interations")

x0 = Power_Method(G, n_iter)
