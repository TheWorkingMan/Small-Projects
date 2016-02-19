#ifndef NODE_H
#define NODE_H

#include <vector>
#include <string>
#include "Edge.h"

class Node {
	std::vector<Edge> edges;
	string ex;
	int val;
public:
	std::vector<Edge> getEdges();
	string getEx();
	int getVal();
};

#endif // !NODE_H
