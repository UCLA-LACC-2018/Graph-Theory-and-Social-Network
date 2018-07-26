#!/usr/bin/python3.6

# Graph Theory easy exercises for Social Networks module
# LACC 2018

#*************************************
# This is where you write your code
#
# matrix_load()
#
# Loads an adjacency matrix for a graph from a file
#
# input: none
# output: matrix containing each node 
# 
# Note: You can open a file using open(filename)
# 
# You can get a list containing each line with file.readlines()
#
#*************************************
def matrix_load(filename):
    mat = [ list(line.strip()) for line in open(filename).readlines() ]
    return [[ int(string) for string in row ] for row in mat ]

mat = matrix_load("matrix.txt")

    #*************************************
# This is where you write your code
#
# print_degrees(mat)
#
# Prints the degrees of all nodes in a graph given an adj. matrix 
#
# input: the adjacency matrix of the graph
# output: none
# 
# Note: You don't need to return anything. 
#
# Effectively, you'll need to count the number of 1s in each row 
# (or each column) and print this. Use a nested loop (for or while)
#*************************************


def print_degrees(mat):
    for row in mat:
        print(row.count(1))

    #*************************************
# This is where you write your code
#
# shortest_path(mat,node1,node2)
#
# Find the shortest path from node1 to node2 of all nodes in a graph given an adj. matrix 
#
# input: the adjacency matrix of the graph,node1,node2
# output: 'The path is: ' appended with all edges on the path if there is one, otherwise print out 'No such path'
# Note: at the same time, return a list containing all the nodes on the path if there is one, otherwise return []
#
#*************************************

def shortest_path(mat,node1,node2):
    path = recur_path(mat, node1, node2, [])
    if (path != None):
        print("The shortest path is:")
        for i in range(len(path) - 1):
            print("(" + str(path[i]) + ", " + str(path[i+1]) + ")")
        return path
    return []

def recur_path(mat, node1, node2, visited):
    if node1 == node2:
        return [node2]
    shortest = None
    old_visited = visited
    visited.append(node1)
    for j in range(len(mat)):
        if mat[node1][j] == 1 and (j not in visited):
            path = recur_path(mat, j, node2, visited)
            if (path != None):
                path.append(node1)
                visited = old_visited
                if (not shortest) or (len(path) < len(shortest)):
                    shortest = path
    return shortest

for row in mat:
    print(row)
print(shortest_path(mat, 1, 4))

    #*************************************
# This is where you write your code
#
# detect_cycle(mat)
#
# Detect the in a graph given an adj. matrix 
#
# input: the adjacency matrix of the graph
# output: 'Find a cycle, the first edge is: ' appended with an arbitrary edge on the cycle if there is one, otherwise print out 'No cycle in the graph'
# 
# Note: at the same time, return a list containing all the nodes on the cycle if there is one, otherwise return []
#
#*************************************

def detect_cycle(mat):
    for i in range(len(mat)):
        path = recur_cycle(mat, i, [])
        if len(path) > 0:
            for i in range(len(path) - 1):
                print("(" + str(path[i]) + ", " + str(path[i+1]) + ")")
            return path
    print("No cycle")
    return []

def recur_cycle(mat, node, visited):
    if len(visited) > 2 and node == visited[0]:
        visited.append(node)
        return visited
    visited.append(node)
    for j in range(len(mat)):
        if mat[node][j] == 1 and (len(visited) < 2 or j != visited[-2]):
            return recur_cycle(mat, j, visited)
    return []

print(detect_cycle(mat))
