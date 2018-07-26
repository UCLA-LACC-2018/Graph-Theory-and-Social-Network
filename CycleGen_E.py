#Extra Exercise for detecting cycles in a graph containing multiple components
#Input: adj. matrix
def detect_cycle_gen(mat):
    conncomp=[]
    cycle=[]
    visited = []
    for i in range(len(mat)) :
        path,nodes = recur_cycle(mat,i,[],[])
        if(len(path) > 0) :
            exists= False
            for j in path:
                if j in visited :
                    exists = True
                
            if(exists == False) :
                for k in path:
                    visited.append(k)
                conncomp.append(nodes)
                cycle.append(path)
    #############################
    #Add your codes here
    #You should compute the values of two variables
    #Suppose the graph contains k connected components G1,...,Gk
    #conncomp is a list, where the i-th component is a list containing all the nodes in Gi
    #cycle is a list, where the i-th component is [] if there is no cycle in Gi,
    #otherwise it should be a list containing the nodes on an arbitrary cycle in Gi
    ############################
    for ind in range(len(conncomp)):
        print('The component consisting of the nodes:\n')
        print(",".join(map(str,conncomp[ind])))
        if cycle[ind]==[]:
            print('has no cycle\n')
        else:
            print('has a cycle consisting of the nodes:\n')
            print(",".join(map(str,cycle[ind])))
    return [conncomp,cycle]
'''
def detect_cycle(mat):
    for i in range(len(mat)):
        path,nodes = recur_cycle(mat, i, [], [])
        if len(path) > 0:
            for i in range(len(path) - 1):
                print("(" + str(path[i]) + ", " + str(path[i+1]) + ")")
            print("All nodes include: " + nodes)
            return path
    print("No cycle")
    print("All nodes include: " + nodes)
    return path
'''
def recur_cycle(mat, node, visited, allnodes):
    allnodes.append(node)
    if len(visited) > 2 and node == visited[0]:
        visited.append(node)
        return visited, allnodes
    visited.append(node)
    for j in range(len(mat)):
        if mat[node][j] == 1 and (len(visited) < 2 or j != visited[-2]):
            return recur_cycle(mat, j, visited, allnodes)
    return [], allnodes