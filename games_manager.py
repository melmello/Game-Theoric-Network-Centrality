from INIT.MatrixUploader import MatrixUploader
from INIT.GraphBuilder import GraphBuilder

# Loading the adjacency matrix and printing it
adjacency_matrix = MatrixUploader().get_matrix()

# Graph construction and visualization
GraphBuilder(adjacency_matrix).graph_construction()

# TODO(melmello): GAME CONSTRUCTION
