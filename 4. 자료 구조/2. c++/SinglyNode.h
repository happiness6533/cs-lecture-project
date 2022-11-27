#pragma once
#include "Node.h"

template <typename Data>
class SinglyNode : public Node<Data> {
private:
	SinglyNode<Data>* nextNodePtr;

public:
	SinglyNode(Data* dataPtr) : Node<Data>(dataPtr) {
		this->nextNodePtr = nullptr;
	}

	SinglyNode<Data>* getNextNodePtr() {
		return nextNodePtr;
	};
	
	void setNextNodePtr(SinglyNode<Data>* nextNodePtr) {
		this->nextNodePtr = nextNodePtr;
	}
};
