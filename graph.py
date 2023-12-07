import random
import copy

from sys import maxsize
from itertools import permutations
def randomGraph(n, maxValue=500, maxLength=100,): #n - number of verticies
    edges = []
    numOfEdges = 0  # max (n * (n - 1))/2
    edgesValues = [[0] * n for _ in range(n)]
    if n<6:
        for i in range(n):
            for j in range(n):
                if i != j:
                    edgesValues[i][j] = random.randint(1,maxValue)
        return edgesValues
    else:
        for i in range(n):
            howManyEdgesFromINotAdded = 0
            for j in range(n):
                if random.randint(0,1) or j==i+1 or howManyEdgesFromINotAdded == n-2:
                    if i != j:
                        edge = [i + 1, j + 1]
                        edges.append(edge)
                        numOfEdges += 1
                else:
                    howManyEdgesFromINotAdded += 1
        edgesValues = [[0] * n for _ in range(n)]
        edgesLengths = [[0] * n for _ in range(n)]
        for j in range(numOfEdges):
            x = edges[j][0] - 1
            y = edges[j][1] - 1
            edgeValue = random.randint(1, maxValue)
            edgeLength = random.randint(1, maxLength)
            edgesValues[x][y] = edgeValue
            edgesValues[y][x] = edgeValue
            edgesLengths[x][y] = edgeLength
            edgesLengths[y][x] = edgeLength

        isVertexAGasStation = [random.randint(0,1) for i in range(n)]

        return [edgesValues,edgesLengths,isVertexAGasStation,numOfEdges]

ggg = randomGraph(5,20,10)
print(ggg)

def greedy(graph,start = 0):
    n = len(graph)
    actV = start
    actNext = []
    actNextVal = []
    visited = [start]
    for i in range(n):
        if graph[actV][i] != 0:
            actNext.append(i)
            actNextVal.append(graph[actV][i])
    actV = actNext[actNextVal.index(min(actNextVal))]
    visited.append(actV)
    wrongAtPos = [[] for _ in range(n+1)]
    while actV!=0:
        actNext = []
        actNextVal = []
        f = 0
        for i in range(n):
            if graph[actV][i] != 0 and i not in visited and i not in wrongAtPos[len(visited)-1]:
                f = 1
                actNext.append(i)
                actNextVal.append(graph[actV][i])
        if f==1:
            actV = actNext[actNextVal.index(min(actNextVal))]
            visited.append(actV)
            if len(visited)==len(graph):
                visited[0] = n+5
        else:
            wrongAtPos[len(visited)-2].append(actV)
            visited.pop()
            actV = visited[-1]
            if len(visited)==len(graph)-1:
                visited[0] = start
    visited[0] = start
    print(visited)

greedy(ggg[0])


def fullPath(tab):
    res = []
    queue = []
    n = len(tab[0])
    v = 0
    next = 0
    last = 0
    actRes = [0]
    while True:
        if actRes==[]:
            break
        elif v==n-1:
            res2 = copy.deepcopy(actRes)
            res.append(res2)
            actRes.pop()
            last = actRes[-1]
            v = actRes[-1]
            next = last
            actRes.pop()
        elif next > n - 1:
            last = v
            actRes.pop()
            next=v+1
            v=actRes[-1]
        elif tab[v][next] > 0:
            v=next
            actRes.append(v)
        next+=1
    res.pop()
    return res

def TSP2(graph, s=0):
    V = len(graph[0])
    print(V)
    # store all vertex apart from source vertex
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)

            # store minimum weight Hamiltonian Cycle
    min_path = maxsize
    next_permutation = permutations(vertex)
    for i in next_permutation:

        # store current Path weight(cost)
        current_pathweight = 0
        current_path = []

        # compute current path weight
        k = s
        current_path.append(k)
        f = 0
        for j in i:
            if graph[k][j] == 0:
                f = 1
                break
            current_pathweight += graph[k][j]
            current_path.append(j)
            k = j
        current_pathweight += graph[k][s]

        # update minimum
        if f==0:
            min_path = min(min_path, current_pathweight)
            if min_path==current_pathweight:
                min_pathh = current_path

    return min_path, min_pathh



V = 6

# implementation of traveling Salesman Problem
def TSP(graph, s=0):
    # store all vertex apart from source vertex
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)

            # store minimum weight Hamiltonian Cycle
    min_path = maxsize
    next_permutation = permutations(vertex)
    for i in next_permutation:

        # store current Path weight(cost)
        current_pathweight = 0

        # compute current path weight
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]

        # update minimum
        min_path = min(min_path, current_pathweight)

    return min_path

#print(TSP(ggg[0]))
#gaga = fullPath(ggg[0])
#print(gaga)

#print(TSP2(ggg[0]))

def values(tab,valTab):
    vallal = []
    for res in tab:
        sum = 0
        for i in range(len(res)-1):
            x = res[i]
            y = res[i+1]
            sum+=valTab[x][y]
        vallal.append(sum)
    return vallal

# def FullTSP(valuesTab):



#gaggg = values(gaga,ggg[0])
#print(gaggg)
#print(min(gaggg))
