#include "Node.h"
#include "Edge.h"
#include <string>

Node::Node(std::string exp) {
	ex = exp;
}

Node::~Node() {}

Edge Node::getEdges() {
	for (Edge &e : edges) {
		return e;
	}
}

std::string Node::getEx() {
	return ex;
}

int Node::getVal() {
	return val;
}