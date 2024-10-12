"""Naive approach
def generateTreeFromPrufer(code):
    code = [i-1 for i in code]
    def nextAvailableNode(code, nodes):
        for i in nodes:
            if i not in code:
                return i
            
    size = len(code) + 2
    nodes = [i for i in range(size)]
    connections = 0
    while connections < size-1:
        if code:
            n = nextAvailableNode(code, nodes)
            print(f"{sorted([n+1, code[0]+1])[0]} {sorted([n+1, code[0]+1])[1]}")
            if len(code) > 1:
                code = code[1:]
            else:
                code = []
            nodes = nodes[0:nodes.index(n)] + nodes[nodes.index(n)+1:]
        else:
            print(f"{sorted([nodes[0]+1, nodes[1]+1])[0]} {sorted([nodes[0]+1, nodes[1]+1])[1]}")
        connections += 1

def printEdges(edgeSet):
    for a, b in edgeSet:
        print(f"{sorted([a,b])[0]} {sorted([a,b])[1]}")
    

t = int(input())
code = list(map(int, input().split()))
generateTreeFromPrufer(code)

"""
import heapq
def generateTreeFromPrufer(code):
    code = [i-1 for i in code]
    size = len(code) + 2
    degree = [1] * size
    
    for node in code:
        degree[node] += 1

    available = []
    for i in range(size):
        if degree[i] == 1:
            heapq.heappush(available, i)

    for node in code:
        leaf = heapq.heappop(available)
        print(f"{leaf+1} {node+1}")

        degree[node] -= 1
        if degree[node] == 1:
            heapq.heappush(available, node)
    
    leaf1 = heapq.heappop(available)
    leaf2 = heapq.heappop(available)
    print(f"{leaf1+1} {leaf2+1}")
    
t = int(input())
code = list(map(int, input().split()))
generateTreeFromPrufer(code)