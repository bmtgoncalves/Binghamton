#!/usr/bin/env python

import numpy as np
from numpy import linalg

from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram
from sklearn.cluster import AgglomerativeClustering

def plot_dendrogram(points, children):
    N, M = children.shape
    new_points = list(points)
    dist = np.zeros(N)

    for i in range(N):
        node_i, node_j = children[i, :]

        pos_i = new_points[node_i]
        pos_j = new_points[node_j]

        new_pos = (pos_i+pos_j)/2.
        new_points.append(new_pos)

        dist[i] = linalg.norm(pos_i-pos_j)

    n_obs = np.arange(2, N+2)

    link_matrix = np.column_stack([children, dist, n_obs]).astype(float)

    dendrogram(link_matrix, distance_sort=True, labels=points)
    plt.xlabel('points')
    plt.ylabel('distance')

points = np.array([[1,2,5,10,11,25]]).T

model = AgglomerativeClustering()
model.fit(points)

plot_dendrogram(points, model.children_)
plt.savefig('agglomerative.png')