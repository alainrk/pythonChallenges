from collections import defaultdict

### FIRST SOLUTION
class Node:
    def __init__(self, infos):
        self.infos = set(infos)

    def addInfo(self, info):
        self.infos.add(info)

def mergeDup(contacts):
    nodes = []
    hmap = {}
    for c in contacts:
        exnode = None
        n = Node(c)
        for info in c:
            if info in hmap:
                exnode = hmap[info]
                break
        if exnode is None:
            nodes.append(n)
            for info in c:
                hmap[info] = n
                n.addInfo(info)
        else:
            for info in c:
                hmap[info] = exnode
                exnode.addInfo(info)
    return nodes

### SECOND SOLUTION

# Directed graph using adjacency list representation
class Graph:
    def __init__(self):
        self.graph = defaultdict(set)
        self.visited = {}

    def addEdge(self,u,v):
        if v is None:
            self.graph[u] = set()
        else:
            self.graph[u].add(v)
        self.visited[u] = False
        self.visited[v] = False


def createGraph(contacts):
    graph = Graph()
    for i,s in enumerate(contacts):
        graph.addEdge(i,None)
        for j,d in enumerate(contacts):
            if i == j:
                continue
            for info in s:
                if info in d:
                    graph.addEdge(i,j)
                    break
    return graph


def connectedComponents(graph, comp, root):
    if not graph.visited[root]:
        graph.visited[root] = True
        comp.append(root)
        for e in graph.graph[root]:
            connectedComponents(graph, comp, e)
    return comp



def merge(contacts):
    graph = createGraph(contacts)
    comps = []
    for node in graph.graph.keys():
        comp = connectedComponents(graph, [], node)
        if len(comp) > 0:
            comps.append(comp)
    return comps


contacts = [[ "John", "john@gmail.com", "john@fb.com"],
            [ "Dan", "dan@gmail.com", "+1234567"],
            [ "Yuota", "didonsan@gmail.com", "dasolo@porco.col"],
            [ "john123", "+5412312", "john123@skype.com"],
            [ "pippo", "+5412312", "john123@skype.com"],
            [ "john123", "+5412312", "pippo@culo.com"],
            [ "john1985", "+555555", "zxczxczxc@culo.con"],
            [ "john1985", "+5412312", "asdasdasd@culo.con"],
            [ "Culo", "+5333333", "dasolo@porco.col"],
            [ "john1985", "+5412312", "123123123@culo.con"],
            [ "john1985", "+111111", "john@fb.com"]]

h = merge(contacts)
for i in h:
    print i
