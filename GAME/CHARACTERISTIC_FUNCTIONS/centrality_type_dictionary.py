""" Type Dictionary

    This dictionary contains the characteristic functions type
    matching a module name to a class name.

"""
from GAME.CHARACTERISTIC_FUNCTIONS.group_degree_centrality \
    import GroupDegreeCentrality
from GAME.CHARACTERISTIC_FUNCTIONS.group_betweenness_centrality \
    import GroupBetweennessCentrality
from GAME.CHARACTERISTIC_FUNCTIONS.group_closeness_centrality \
    import GroupClosenessCentrality

TYPE_TO_CLASS = {
    'group_degree_centrality': GroupDegreeCentrality,
    'group_betweenness_centrality': GroupBetweennessCentrality,
    'group_closeness_centrality': GroupClosenessCentrality
}
