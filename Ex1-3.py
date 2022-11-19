adjacency_matrix = []
adjacency_matrix_index = {}
adjacency_list = {}
edge_list = []


def add_node(name):
    adjacency_list[name] = []
    adjacency_matrix_index[name] = len(adjacency_matrix_index)
    adjacency_matrix.append([0] * len(adjacency_matrix))
    for row in adjacency_matrix:
        row.append(0)


def add_edge(node1, node2):
    adjacency_list[node1].append(node2)
    adjacency_list[node2].append(node1)
    edge_list.append((node1, node2))
    node1 = adjacency_matrix_index[node1]
    node2 = adjacency_matrix_index[node2]
    adjacency_matrix[node1][node2] = 1
    adjacency_matrix[node2][node1] = 1


def remove_edge(node1, node2):
    adjacency_list[node1].remove(node2)
    adjacency_list[node2].remove(node1)
    edge_list.remove((node1, node2))
    node1 = adjacency_matrix_index[node1]
    node2 = adjacency_matrix_index[node2]
    adjacency_matrix[node1][node2] = 0
    adjacency_matrix[node2][node1] = 0


def show_graph():
    print("------------------------------------")
    print("Adjacency Matrix:\n")
    nodename = []
    print(" ", end="")
    for index in adjacency_matrix_index:
        nodename += [index]
        print(" " + index, end="")
    print()
    for index in range(len(adjacency_matrix)):
        row = adjacency_matrix[index]
        print(nodename[index], end="")
        print(" ", end="")
        print(*row)

    print()
    print("------------------------------------")
    print("Adjacency List:\n")
    for key, value in adjacency_list.items():
        print(f"{key}: {' '.join(value)}")

    print()
    print("------------------------------------")
    print("Edge List:\n")
    for index in range(len(edge_list)):
        start = edge_list[index][0]
        end = edge_list[index][1]

        print(f"{index}: {start} {end} [{start}/{end}]")

    print("------------------------------------")


def Ex1():
    add_node("A")
    add_node("B")
    add_node("C")
    add_node("D")
    add_edge("A", "B")
    add_edge("A", "C")
    add_edge("B", "C")
    add_edge("C", "D")
    show_graph()


def Ex2():
    add_node("A")
    add_node("B")
    add_node("C")
    add_node("D")
    add_node("E")
    add_node("F")
    add_edge("A", "B")
    add_edge("A", "C")
    add_edge("A", "F")
    add_edge("C", "D")
    add_edge("D", "E")
    add_edge("E", "F")
    show_graph()


def Ex3():
    node = ["A", "B", "C", "D", "E", "F"]
    for i in node:
        add_node(i)
    add_edge("A", "B")
    add_edge("A", "C")
    add_edge("C", "D")
    add_edge("C", "F")
    add_edge("E", "F")
    show_graph()
    remove_edge("C", "F")
    remove_edge("A", "B")
    remove_edge("C", "D")
    show_graph()
    add_edge("A", "E")
    add_edge("B", "C")
    add_edge("D", "F")
    show_graph()


# Ex1()
# Ex2()
# Ex3()
def main():
    print("1. Example 1")
    print("2. Example 2")
    print("3. Example 3")
    print("4. Exit")
    while True:
        adjacency_matrix.clear()
        adjacency_matrix_index.clear()
        adjacency_list.clear()
        edge_list.clear()
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                Ex1()
            elif choice == 2:
                Ex2()
            elif choice == 3:
                Ex3()
            elif choice == 4:
                break
            else:
                print("Invalid choice")
        except:
            print("Invalid choice")


main()