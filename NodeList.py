import Nodes


class NodeHolder:
    def __init__(self, node: Nodes.Node, userPos: int):
        self.node = node
        self.userPos = userPos

    def __str__(self):
        return f"{self.userPos}\t{self.node}"


class List:
    def __init__(self, name, nodes: list[Nodes.Node]):
        self.name = name
        self.nodes: list[NodeHolder] = [NodeHolder(b, a) for a, b in enumerate(nodes)]
        for node in nodes:
            node.lists.add(name)

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

    def __str__(self):
        sAcc = f"{self.name}\nOrder\tName\tNotes\tLists\tShared\tCompletable\tCompletion\tTime\n"
        for node in self.nodes:
            sAcc += str(node) + "\n"
        sAcc.rstrip()
        return sAcc


if __name__ == "__main__":
    a = Nodes.Node("thing", time=Nodes.Time(8, 8, 8))
    thing = List(
        "A List",
        [
            Nodes.Node("hats", lists={"klfja", "kajsdf;lka"}, time=Nodes.Time(15, 20, 70)),
            Nodes.Node("beans", time=Nodes.Time(10, 5, 2)),
            Nodes.Node("Cheese", time=Nodes.Time(11, 51, 21)),
            a,
            Nodes.Node("mmm"),
        ],
    )
    thing2 = List("B List", [a, Nodes.Node("chee")])
    print(thing)
    thing.sort("time")
    print(thing)
    print()
    print(thing2)
