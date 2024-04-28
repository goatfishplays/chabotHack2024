import Nodes
import json


class NodeHolder:
    def __init__(self, node: Nodes.Node, userPos: int):
        self.node = node
        self.userPos = userPos

    def __str__(self):
        return f"{self.userPos}\t{self.node}"


class List:
    nodePool: list[Nodes.Node] = list()

    def __init__(self, name="No Name", nodes: list[Nodes.Node] = [], addToLists=True):
        self.name = name
        self.nodes: list[NodeHolder] = [NodeHolder(b, a) for a, b in enumerate(nodes)]
        for node in nodes:
            if node not in List.nodePool:
                List.nodePool.append(node)
        if addToLists:
            for node in nodes:
                node.lists.add(name)
                node.updateFile()

    def updateFile(self):
        with open("./Lists/" + self.name + ".json", "w") as f:
            self.sort()
            data = {"name": self.name, "items": tuple([(x.userPos, x.node.name) for x in self.nodes])}
            # print(data)
            json.dump(data, f)

    def loadFile(self, name):
        with open("./Lists/" + name + ".json", "r") as rawRead:
            f = json.load(rawRead)
            self.name = f["name"]
            self.nodes = []
            # print(f["items"])
            for userInd, nodeName in f["items"]:
                for node in List.nodePool:
                    if node.name == nodeName:
                        self.nodes.append(NodeHolder(node, userInd))
                        break
                else:
                    nTemp = Nodes.Node()
                    # print(nodeName)
                    nTemp.loadFile(nodeName)
                    self.nodes.append(NodeHolder(nTemp, userInd))

    def sort(self, sortType: str = "", reverse: bool = False):
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

    def __str__(self):
        sAcc = f"{self.name}\nOrder\tName\tNotes\tLists\tShared\tCompletable\tCompletion\tTime\n"
        for node in self.nodes:
            sAcc += str(node) + "\n"
        sAcc.rstrip()
        return sAcc


if __name__ == "__main__":
    # a = Nodes.Node("thing", time=Nodes.Time(8, 8, 8))
    # thing = List(
    #     "A List",
    #     [
    #         Nodes.Node("hats", lists={"klfja", "kajsdf;lka"}, time=Nodes.Time(15, 20, 70)),
    #         Nodes.Node("beans", time=Nodes.Time(10, 5, 2)),
    #         Nodes.Node("Cheese", time=Nodes.Time(11, 51, 21)),
    #         a,
    #         Nodes.Node("mmm"),
    #     ],
    # )
    # thing2 = List("B List", [a, Nodes.Node("chee")])
    # print(thing)
    # thing.sort("time")
    # print(thing)
    # thing.updateFile()
    # print()
    # print(thing2)

    thingLoad = List()
    thingLoad.loadFile("A List")
    print(thingLoad)
