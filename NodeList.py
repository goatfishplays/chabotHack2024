import Nodes

class NodeHolder:
    def __init__(self, node, userPos):
        self.node = node
        self.userPos = userPos

class List:
    def __init__(self, nodes):
        self.nodes: list = [NodeHolder(b, a) for a,b in enumerate(nodes)]


    def sort(self, sortType):
        match sortType:
            case "time":
                self.nodes.sort(key)