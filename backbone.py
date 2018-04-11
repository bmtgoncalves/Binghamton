#!/usr/bin/env python

from sys import argv, stderr
import networkx as NX

def backbone(network_file, alpha = 0.9):
    strength = {} 
    
    for line in open(network_file):
        fields = line.strip().split()
        
        node_i = fields[0]
        node_j = fields[1]
        weight = float(fields[2])
        
        strength[node_i] = strength.get(node_i, 0) + weight
        strength[node_j] = strength.get(node_j, 0) + weight
    
    G = NX.Graph()
    G3 = NX.Graph()
    
    for line in open(network_file):
        fields = line.strip().split()
        
        node_i = fields[0]
        node_j = fields[1]
        weight = float(fields[2])
        
        if node_i != node_j:
            frac_weight = weight/strength[node_i]
            
            G.add_edge(node_i, node_j, weight = frac_weight)
            G3.add_edge(node_i, node_j, weight = weight)
    
    G2 = NX.Graph()
    
    for node_i, node_j in G.edges():
        if G[node_i][node_j]["weight"] > 0. and G.degree(node_i) > 1:
            fraction = 1. - (1. -\
            G[node_i][node_j]["weight"])**(float(G.degree(node_i)) - 1.)\
            
            G2.add_edge(node_i, node_j, weight = 1. - fraction)
    
    for node_i, node_j in G3.edges():
        if G3[node_i][node_j]["weight"] > 0.:
            try:                
                if G2[node_i][node_j]["weight"] < alpha:
                    print node_i, node_j, G3[node_i][node_j]["weight"]
                    
            except Exception, e:
                continue

if __name__ == "__main__":
    if len(argv) == 3:
        backbone(argv[1], float(argv[2]))
    else:
        backbone(argv[1])
