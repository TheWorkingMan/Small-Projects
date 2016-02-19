#ifndef GRAPH_H
#define GRAPH_H

#include <vector>
#include "Node.h"
#include "Edge.h"

class Graph {
	std::vector<Node> nodes;
public:
	Graph() {};
	~Graph() {};
	void addEdge(Node a, Node b);
	std::vector<Node> printGraph();
};

#endif // !GRAPH_H
