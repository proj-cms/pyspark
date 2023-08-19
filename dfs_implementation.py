from collections import defaultdict
from typing import List

class MyGraph:
    # define init dundr
    def __init__(self):
        print("calling init")
        self.graph = defaultdict(list)

    # define method for adding edges

    def addEdge(self, edge, vertex):
        self.graph[edge].append(vertex)

    # dfs method will get root as start point then it has to start trversing
    # from that
    def dfs(self,edge,visited_array:List):





if __name__ == "__main__":
    g = MyGraph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)





