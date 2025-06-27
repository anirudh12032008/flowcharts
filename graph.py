class Node:
    def __init__(self, id, label, type, shape):
        self.id = id
        self.label = label
        self.type = type
        self.shape = shape


class Edge:
    def __init__(self, source, target):
        self.source = source
        self.target = target


class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = []

    def add(self, node, label, type, shape):
        if node in self.nodes:
            return
        self.nodes[node] = Node(node, label, type, shape)

    def connect(self, source, target):
        if source not in self.nodes or target not in self.nodes:
            return
        self.edges.append(Edge(source, target))



def render(graph):
    print("Flowchrt")

    visit = set()

    def draw(label, shape):
        if shape == "circle":
            return f"({label})"
        elif shape == "square":
            return f"[{label}]"
        elif shape == "diamond":
            return f"<{label}>"
        elif shape == "cloud":
            return f"{{{label}}}"
        else:
            return f"{label}"
    
    def dfs(id):
        visit.add(id)

        node = graph.nodes[id]
        print(draw(node.label, node.shape))

        for edge in graph.edges:
            if edge.source == id:
                print("  |")
                print("  V")
                dfs(edge.target)

    everything = {e.target for e in graph.edges}
    roots = [n for n in graph.nodes if n not in everything]
    for root in roots:
        dfs(root)
        print("")




g = Graph()
g.add("A", "Start", "process", "circle")
g.add("B", "Think", "action", "cloud")
g.add("C", "Do", "process", "square")

g.connect("A", "B")
g.connect("B", "C")

render(g)

