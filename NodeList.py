import Nodes
import json


class NodeHolder:
    def __init__(self, node: Nodes.Node, userPos: int):
        self.node = node
        self.userPos = userPos

    def __str__(self):
        return f"{self.userPos}\t{self.node.defaultView()}"


class NodeList:
    nodePool: list[Nodes.Node] = list()

    def __init__(self, name="No Name", nodes: list[Nodes.Node] = [], addToNodeLists=True):
        self.name = name
        self.nodes: list[NodeHolder] = [NodeHolder(b, a) for a, b in enumerate(nodes)]
        for node in nodes:
            if node not in NodeList.nodePool:
                NodeList.nodePool.append(node)
        if addToNodeLists:
            for node in nodes:
                node.lists.add(name)
                node.updateFile()

    def updateFile(self):
        with open("./NodeLists/" + self.name + ".json", "w") as f:
            self.sort()
            data = {"name": self.name, "items": tuple([(x.userPos, x.node.name) for x in self.nodes])}
            # print(data)
            json.dump(data, f)

    def loadFile(self, name):
        with open("./NodeLists/" + name, "r") as rawRead:
            f = json.load(rawRead)
            self.name = f["name"]
            self.nodes = []
            # print(f["items"])
            for userInd, nodeName in f["items"]:
                # print(userInd, nodeName)
                for node in NodeList.nodePool:
                    if node.name == nodeName:
                        self.nodes.append(NodeHolder(node, userInd))
                        break
                else:
                    nTemp = Nodes.Node()
                    # print(nodeName)
                    nTemp.loadFile(nodeName + ".json")
                    self.nodes.append(NodeHolder(nTemp, userInd))

    def sort(self, sortType: str = "", reverse: bool = False):
        # TODO: Add more sortTypes
        if sortType == "time":
            self.nodes.sort(key=lambda x: x.node.getTimeSecs())
        else:
            self.nodes.sort(key=lambda x: x.userPos)
        if reverse:
            self.nodes.reverse()

    def removeNode(self, node: Nodes.Node):
        for i in range(len(self.nodes)):
            if self.nodes[i].node == node:
                node.lists.remove(self.name)
                self.nodes.pop(i)
                return

    def addNode(self, node: Nodes.Node):
        self.nodes.append(NodeHolder(node, len(self.nodes)))

    def moveNode(self, oldPos, pos):
        if pos < 0 or pos > len(self.nodes) or oldPos < 0 or oldPos > len(self.nodes):
            print("Out of bounds")
            return
        for node in self.nodes:
            if oldPos == node.userPos:
                node.userPos = pos
            elif node.userPos > oldPos and pos >= node.userPos:
                node.userPos -= 1
            elif node.userPos < oldPos and pos <= node.userPos:
                node.userPos += 1

    def __str__(self):
        sAcc = f"{self.name}\nOrder\tName\tValue\tTime\n"
        for node in self.nodes:
            sAcc += str(node) + "\n"
        sAcc.rstrip()
        return sAcc


if __name__ == "__main__":
    pass
    # a = Nodes.Node("thing", time_hour=8, time_min=8, time_sec=8)
    # thing = NodeList(
    #     "A NodeList",
    #     [
    #         Nodes.Node("hats", lists={"klfja", "kajsdf;lka"}, time_hour=15, time_min=70, time_sec=20),
    #         Nodes.Node("beans", time_hour=20, time_min=15, time_sec=10),
    #         Nodes.Node("Cheese", time_hour=100, time_min=99, time_sec=7000),
    #         a,
    #         Nodes.Node("mmm"),
    #     ],
    # )
    # thing2 = NodeList("B NodeList", [a, Nodes.Node("chee")])
    # print(thing)
    # thing.sort("time")
    # print(thing)
    # thing.updateFile()
    # print()
    # print(thing2)

    # thingLoad = NodeList()
    # thingLoad.loadFile("A NodeList.json")
    # print(thingLoad)
