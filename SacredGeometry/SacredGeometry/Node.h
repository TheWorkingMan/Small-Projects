#ifndef NODE_H
#define NODE_H

#include <vector>
#include <string>
#include "Edge.h"

class Node {
	std::vector<Edge> edges;
	std::string ex;
	int val;
public:
	Node(std::string exp);
	~Node();
	Edge getEdges();
	std::string getEx();
	int getVal();
};

#endif // !NODE_H
