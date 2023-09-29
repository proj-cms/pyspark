import pprint
from collections import defaultdict
from typing import List


class MyGraph:
    # define init dundr
    def __init__(self):
        self.graph = defaultdict(list)

    # define method for adding edges

    def addEdge(self, edge, vertex):
        if vertex:
            self.graph[edge].append(vertex)
        else:
            self.graph[edge] = []

    # dfs method will get root as start point then it has to start traversing
    # from that
    def dfs(self,edge,visited_array:List):
        visited_array.append(edge)
        print(edge)

        for node in self.graph[edge]:
            if node not in visited_array:
                self.dfs(node,visited_array)

    #def check_2_employee_manager(self,edge1,edge2):

if __name__ == "__main__":
    g = MyGraph()
    # edge is the name of employee
    g.addEdge('ceo_1', 'emp_1')
    g.addEdge('ceo_1', 'emp_2')
    g.addEdge('ceo_2', 'emp_3')
    g.addEdge('emp_2', 'emp_4')
    g.addEdge('emp_2', 'emp_5')
    g.addEdge('emp_5', 'emp_6')
    g.addEdge('emp_6',None)
    graph_len = len(g.graph)
    # initialize an array for visited node
    visited_array = []
    pprint.PrettyPrinter(width=20).pprint(g.graph)
    #g.dfs('ceo_1',visited_array)







