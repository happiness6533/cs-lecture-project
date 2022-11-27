#pragma once
#include "Node.h"
#include "Data.h"
#include "DoublyNode.h"
#include "DoublyLinkedList.h"

template <typename TData, typename Key>
class GraphNode : public Node<TData>, public Data<Key> {
private:
	bool visitStatus;
	DoublyLinkedList<GraphNode<TData, Key>>* adjacentNodeList;

public:
	GraphNode(TData* dataPtr) : Node<TData>(dataPtr), Data<Key>(dataPtr->getKey()) {
		visitStatus = false;
		adjacentNodeList = new DoublyLinkedList<GraphNode<TData, Key>>();
	}

	bool getVisitStatus() {
		return visitStatus;
	}

	void setVisitStatus(bool visitStatus) {
		this->visitStatus = visitStatus;
	}

	DoublyLinkedList<GraphNode<TData, Key>>* getAdjacentNodeList() {
		return adjacentNodeList;
	}

	void addAdjacentNode(GraphNode<TData, Key>* graphNodePtr) {
		adjacentNodeList->addData(graphNodePtr);
	}
};
