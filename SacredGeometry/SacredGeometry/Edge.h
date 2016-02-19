#ifndef EDGE_H
#define EDGE_H

#include "Node.h"

class Edge {
	Node *dest;
	int weight;
public:
	Edge() {};
	~Edge() {};
};

#endif // !EDGE_H
