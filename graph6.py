import math
import random
import copy

from sys import maxsize
from itertools import permutations

# algorytm przechodzi z każdego wieszchołka losowo przez wszytkie pozostałe wieszchołki i wraca twożąc cykl i krawędzie
def randomGraph(n, maxValue=500, fuel=50): #n - number of verticies
    minValue = math.floor(fuel/(n-1))
    cycles = []
    isAGasStation = [0 for i in range(n)]
    verticies = [int(i) for i in range(n)]
    edgesValues = [[0] * n for _ in range(n)]
    for i in range(n):
        actFuel = fuel
        actPath = [i]
        actVert = copy.deepcopy(verticies)
        actVert.remove(i)

        #Twoży krawędzie
        for j in range(n-1):
            act=actPath[-1]
            next = random.randint(0,len(actVert)-1)
            nextVal = random.randint(minValue,maxValue)
            nextVert = actVert[next]
            if edgesValues[act][nextVert]!=0:
                nextVal = edgesValues[act][nextVert]
            if actFuel-nextVal<=0:
                diff = nextVal-actFuel
                nextVal -= diff
                isAGasStation[nextVert] = 1
                actFuel = fuel
            else:
                actFuel -= nextVal
            actPath.append(actVert[next])
            actVert.remove(actVert[next])
            edgesValues[act][nextVert] = nextVal
            edgesValues[nextVert][act] = edgesValues[act][nextVert]
        #wpisuje krawędzie do macieży z wartościami przejazdu
        if edgesValues[actPath[-1]][i]!= 0:
            nextVal = edgesValues[actPath[-1]][i]
        else:
            nextVal = random.randint(1,maxValue)
        if actFuel-nextVal>=0:
            edgesValues[actPath[-1]][i] = nextVal
            edgesValues[i][actPath[-1]] = nextVal
        else:
            edgesValues[actPath[-1]][i] = nextVal-actFuel
            edgesValues[i][actPath[-1]] = nextVal - actFuel
        cycles.append(actPath)
    return [edgesValues,cycles,isAGasStation]

ggg = randomGraph(5,20,20)
print(ggg)

def greedy(graph,fuel,isAGasStation,start = 0):
    n = len(graph)
    actV = start    #aktualny wieszchołek
    actNext = []    #sąsiedzi w każdym etapie
    actNextVal = [] #koszty sąsiadów w każdym etapie
    visited = [start]   #odwiedzone wieszchołki
    for i in range(n):  #od 0 do n
        if graph[actV][i] != 0: #jeżeli istnieje krawędź
            actNext.append(i)   #dodaj sąsiada
            actNextVal.append(graph[actV][i])   #dodaj wartość sąsiadza
    actV = actNext[actNextVal.index(min(actNextVal))]   #wybierz sąsiada z najmniejszym kosztem
    visited.append(actV)    #dodaj wybrany wieszchołek do odwiedzonych
    wrongAtPos = [[] for _ in range(n+1)]   #wieszchołki odwiedzone na danym etapie, ale wrócone z nich
    actFuel = fuel  #aktualne paliwo równa się paliwo
    while actV!=start:  #dopóki aktualny wieszchołke znowu nie równa sie start
        actNext = []    #zeruje sąsiadów
        actNextVal = [] #zeruje wartości sąsiadów
        f = 0           # flaga czy jakikolwiek wieszchołek z sąsiadów się nadaje
        for i in range(n):  #od 0 do n
            if graph[actV][i] != 0 and i not in visited and i not in wrongAtPos[len(visited)-1]:    #jeżeli istnieje krawędż i sąsaid nie jest w odwiedzonych i nie jest w złych
                f = 1
                actNext.append(i)   #dodaj sąsiada
                actNextVal.append(graph[actV][i])   #dodaj wartość sąsiada
        if f==1:    #jeżeli są jacyś mozliwi sąsziedzi
            nextV = actNext[actNextVal.index(min(actNextVal))]
            if actFuel - graph[actV][nextV] <= 0 and isAGasStation[actV] == 0:  #jeżeli paliwo po przejechaniu do sąsiadza >= 0
                wrongAtPos[len(visited) - 1].append(nextV)
                if len(visited) == len(graph) - 1:
                    visited[0] = start
            elif actFuel - graph[actV][nextV] <= 0 and isAGasStation[actV] == 1:
                actFuel = fuel
                actV = nextV
                visited.append(actV)
                if len(visited) == len(graph):
                    visited[0] = n + 5
            else:
                actFuel -= graph[actV][nextV]
                actV = nextV
                visited.append(actV)
                if len(visited)==len(graph):
                    visited[0] = n+5
        else:       #jeżeli nie ma możliwych sąsisiadów
            actFuel += graph[actV][visited[-2]]
            wrongAtPos[len(visited)-2].append(actV)
            visited.pop()
            actV = visited[-1]
            if len(visited)==len(graph)-1:
                visited[0] = start
    visited[0] = start
    print(visited)

greedy(ggg[0],30,ggg[2])


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
