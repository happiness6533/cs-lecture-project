#pragma once
#include "Node.h"

template <typename Data>
class DoublyNode : public Node<Data> {
private:
	DoublyNode<Data>* nextNodePtr;
	DoublyNode<Data>* previousNodePtr;

public:
	DoublyNode(Data* dataPtr) : Node<Data>(dataPtr) {
		this->nextNodePtr = nullptr;
		this->previousNodePtr = nullptr;
	}

	DoublyNode<Data>* getNextNodePtr() {
		return nextNodePtr;
	}

	void setNextNodePtr(DoublyNode<Data>* nextNodePtr) {
		this->nextNodePtr = nextNodePtr;
	}

	DoublyNode<Data>* getPreviousNodePtr() {
		return previousNodePtr;
	}

	void setPreviousNodePtr(DoublyNode<Data>* previousNodePtr) {
		this->previousNodePtr = previousNodePtr;
	}
};
