import NodeList
import Nodes
import os

list_pool: list[NodeList.NodeList] = []


def main_hub():
    while True:
        print()

        print("Select an action")
        print("[1] Lists Menu")
        print("[2] Nodes Menu")
        print("[3] Load Nodes and Lists")
        print("[-1] End")
        choice = int(input())
        match choice:
            case 1:
                lists_hub()
            case 2:
                nodes_hub()
            case 3:
                load_stuffs()
            case -1:
                return


def load_stuffs():
    # print(os.listdir("./NodeLists/"))
    for n in os.listdir("./Nodes/"):
        try:
            # print(n)
            tempN = Nodes.Node()
            tempN.loadFile(n)
            NodeList.NodeList.nodePool.append(tempN)
        except:
            print(f"Could not load {n}")
    for l in os.listdir("./NodeLists/"):
        try:
            tempNL = NodeList.NodeList()
            tempNL.loadFile(l)
            list_pool.append(tempNL)
        except:
            print(f"Could not load {n}")


def lists_hub():
    while True:
        print()

        print("Select an action")
        print("[1] List Lists")
        print("[2] View List")
        print("[3] Create/Edit List")
        print("[-1] Exit")
        choice = int(input())
        match choice:
            case 1:
                list_lists()
            case 2:
                view_list()
            case 3:
                edit_list()
            case -1:
                return


def list_lists():
    print()
    if len(list_pool) == 0:
        print("Nothing to show")
    for l in list_pool:
        print(l.name)


def view_list():
    print("Please input the name of the list")
    listName = input()
    for l in list_pool:
        if l.name == listName:
            l.sort(input("Please enter the sort type(index, time, ): "), input("Reverse(y/n): ") == "y")
            print(l)
            l.sort()
            break
    else:
        print("List name invalid")


def edit_list():
    print("Please input the name of the list")
    listName = input()
    selList = None
    for l in list_pool:
        if l.name == listName:
            selList = l
            break
    else:
        print("Creating List.")
        selList = NodeList.NodeList(listName)
        list_pool.append(selList)

    while True:
        print()
        print(selList)
        print()
        print("What action would you like to take for " + selList.name)
        print("[1] Append Node")
        print("[2] Insert Node")
        print("[3] Move Node")
        print("[4] Remove Node")
        print("[-1] Exit")
        choice = int(input())
        match choice:
            case 1:
                selList.addNode(get_node_for_list())
            case 2:
                # selNode = get_node_for_list()
                selList.addNode(get_node_for_list())
                selList.moveNode(len(selList.nodes) - 1, int(input("Pos: ")))
            case 3:
                selList.moveNode(int(input("Old Pos: ")), int(input("New Pos: ")))
            case 4:
                print("Please enter the name of the node")
                name = input()
                for node in NodeList.NodeList.nodePool:
                    if node.name == name:
                        selList.removeNode(node)
                        break
                else:
                    print("Node not found")
            case -1:
                selList.updateFile()
                return
        print("New List:")
        selList.updateFile()


def get_node_for_list():
    print("Please enter the name of the node")
    name = input()
    selNode = None
    for node in NodeList.NodeList.nodePool:
        if node.name == name:
            selNode = node
            break
    else:
        print("Creating node")

        selNode = Nodes.Node(
            name,
            input("Description: "),
            {name},
            False,
            input("Completable(no, perc, count): "),
            int(input("Amount Completed: ")),
            int(input("Hours till(negative if untimed): ")),
            int(input("Mins till(negative if untimed): ")),
            int(input("Secs till(negative if untimed): ")),
            input("Date Rule Code: "),
        )
        NodeList.NodeList.nodePool.append(selNode)
        selNode.updateFile()
    return selNode


def nodes_hub():
    while True:
        print()

        print("Select an action")
        print("[1] List Nodes")
        print("[2] View Node")
        print("[3] Create/Edit Node")
        print("[-1] Exit")
        choice = int(input())
        match choice:
            case 1:
                list_nodes()
            case 2:
                view_node()
            case 3:
                edit_node()
            case -1:
                return


def list_nodes():
    print()

    if len(NodeList.NodeList.nodePool) == 0:
        print("Nothing to show")
    for node in NodeList.NodeList.nodePool:
        print(node.name)


def view_node():
    print()

    print("Please input the name of the node")
    nodeName = input()
    for n in NodeList.NodeList.nodePool:
        if n.name == nodeName:
            print(n)
            break
    else:
        print("Node name invalid")


def edit_node():
    print()

    print("Please input the name of the node")
    name = input()
    selNode = None
    for n in NodeList.NodeList.nodePool:
        if n.name == name:
            selNode = n
            break
    else:
        print("Creating node.")
        selNode = Nodes.Node(
            name,
            input("Description: "),
            {},
            False,
            input("Completable(no, perc, count): "),
            int(input("Amount Completed: ")),
            int(input("Hours till(negative if untimed): ")),
            int(input("Mins till(negative if untimed): ")),
            int(input("Secs till(negative if untimed): ")),
            input("Date Rule Code: "),
        )
        selNode.updateFile()
        NodeList.NodeList.nodePool.append(selNode)
    while True:
        print()
        print(selNode)
        print()
        print("What action would you like to take for " + selNode.name)
        print("[1] Change Description")
        print("[2] Change Completion Type")
        print("[3] Change Amount Completed")
        print("[4] Change Relative Time")
        print("[5] Change Absolute Time")
        print("[-1] Exit")
        choice = int(input())
        match choice:
            case 1:
                selNode.notes = input("New description: ")
            case 2:
                selNode.completable = input("Completable(no, perc, count): ")
            case 3:
                selNode.completion = int(input("Amount Completed: "))
            case 4:
                selNode.setRelativeTime(int(input("Hours till(negative if untimed): ")), int(input("Mins till(negative if untimed): ")), int(input("Secs till(negative if untimed): ")))
            case 5:
                selNode.time_hour = int(input("Hours till(negative if untimed): "))
                selNode.time_min = int(input("Mins till(negative if untimed): "))
                selNode.time_sec = int(input("Secs till(negative if untimed): "))
                selNode.reformat_time()
            case -1:
                selNode.updateFile()
                return
        print("New Node:")
        selNode.updateFile()


# def create_node(name, notes, lists, shared, completable, completion, time_hour, time_min, time_sec, dateRules):
#     return Nodes.Node(name, notes, lists, shared, completable, int(completion), int(time_hour), int(time_min), int(time_sec), dateRules)


main_hub()
