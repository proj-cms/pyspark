import sys
from heapq import heapify, heappush, heappop


def dijsktra(graph, src, dest):
    inf = sys.maxsize
    # create a data structure to store the cost and predecessor
    node_data = {'A': {'cost': inf, 'pred': []},
                 'B': {'cost': inf, 'pred': []},
                 'C': {'cost': inf, 'pred': []},
                 'D': {'cost': inf, 'pred': []},
                 'E': {'cost': inf, 'pred': []},
                 'F': {'cost': inf, 'pred': []}
                 }
    # assign source node cost to ZERO as its starting node
    node_data[src]['cost'] = 0
    visited = []
    temp = src # assign the source node to temp
    for i in range(5): # this range is decided b the number of nodes - 1
        if temp not in visited:
            visited.append(temp)
            min_heap = []
            for j in graph[temp]: # iterate over all connecting nodes of current node
                if j not in visited:
                    # calculate the cost as cost till now + cost from graph so the each node get accumulated ocst
                    cost = node_data[temp]['cost'] + graph[temp][j]
                    if cost < node_data[j]['cost']:
                        node_data[j]['cost'] = cost
                        node_data[j]['pred'] = node_data[temp]['pred'] + [temp]
                    heappush(min_heap, (node_data[j]['cost'], j))
        heapify(min_heap)
        # print (f'checking heap : {min_heap}')
        temp = min_heap[0][1] # Reassign source
    print("Shortest Distance: " + str(node_data[dest]['cost']))
    print("Shortest Path: " + str(node_data[dest]['pred'] + list(dest)))


if __name__ == "__main__":
    graph = {
        'A': {'B': 2, 'C': 4},
        'B': {'A': 2, 'C': 3, 'D': 8},
        'C': {'A': 4, 'B': 3, 'E': 5, 'D': 2},
        'D': {'B': 8, 'C': 2, 'E': 11, 'F': 22},
        'E': {'C': 5, 'D': 11, 'F': 1},
        'F': {'D': 22, 'E': 1}
    }

    source = 'A'
    destination = 'F'
    dijsktra(graph, source, destination)
