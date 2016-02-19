#include "Edge.h"
#include "Node.h"

Edge::Edge() {
	dest = NULL;
	weight = NULL;
}

Edge::~Edge() {
	delete dest;
}