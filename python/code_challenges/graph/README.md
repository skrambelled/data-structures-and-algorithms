# Graphs

Graphs are a datastructure comprised of nodes that at interconnect in a network.

## Methods

`add_node(value)` - add a node/vertex with given value

`get_nodes()` - return a list of all the nodes/vertices in the Graph

`add_edge(start, end, weight)` - creates an Edge connecting two node. Optionally, you can supply some `weight`, which will ootherwise be set to 0

`get_neightbords(vertex)` - returns a list of all the neigbords of a given node/vertex

`size()` - retuns the number of nodes

`breadth_first(vertex)` - perform a breadth first traversal, starting at the supplied vertex, and return all the connected vertices

`connected(first, second)` - test to see if the first vertex is connect to the second vertex
