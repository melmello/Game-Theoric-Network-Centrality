import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


class GraphBuilder:

    def __init__(self, matrix):
        self.matrix = matrix


def graph_construction(matrix):
    """ [OPTIONAL] Function crating the graph visualized

        The system takes the matrix object and builds the graph, specifying the nodes number and the edges.
        Notice that this is used only to have a graphic feedback and thus this function can be avoided
        speeding up the program.

        Args:
            matrix (matrix): this is the matrix object of the matrix file chosen by the user

        Returns:
            no returns are required
    """
    # Counting nodes
    nodes_number = matrix.shape[0]

    # Get the row and column coordinates where the ith and jth element is 1
    rows, cols = np.where(matrix == 1)

    # Rearranges the list of rows and columns into a list of edge tuples.
    # Printing all starting nodes
    # Printing all ending nodes
    # Printing all edges
    # F means FROM, T means TO
    edges = zip(rows.tolist(), cols.tolist())
    print("F nodes:", np.arange(matrix.shape[0]))
    print("T nodes:", np.arange(matrix.shape[1]))
    print("Edges:")
    for x, y in zip(rows.tolist(), cols.tolist()):
        print((x, y))

    # Create a Directed Graph Object adding the nodes and the edges previously calculated
    directed_graph = nx.DiGraph()
    directed_graph.add_nodes_from(range(nodes_number))
    directed_graph.add_edges_from(edges)

    # Printing
    pos = nx.drawing.layout.circular_layout(directed_graph)
    nx.draw_networkx(directed_graph, pos=pos)
    plt.axis('off')
    plt.show()
