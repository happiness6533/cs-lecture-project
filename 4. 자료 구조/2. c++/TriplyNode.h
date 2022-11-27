#pragma once
#include "Node.h"

template <typename Data>
class TriplyNode : public Node<Data> {
private:
	TriplyNode<Data>* motherNodePtr;
	TriplyNode<Data>* nextNodePtr;
	TriplyNode<Data>* previousNodePtr;

public:
	TriplyNode(Data* dataPtr) : Node<Data>(dataPtr) {
		this->motherNodePtr = nullptr;
		this->nextNodePtr = nullptr;
		this->previousNodePtr = nullptr;
	}

	TriplyNode<Data>* getMotherNodePtr() {
		return motherNodePtr;
	}

	void setMotherNodePtr(TriplyNode<Data>* motherNodePtr) {
		this->motherNodePtr = motherNodePtr;
	}

	TriplyNode<Data>* getNextNodePtr() {
		return nextNodePtr;
	}

	void setNextNodePtr(TriplyNode<Data>* nextNodePtr) {
		this->nextNodePtr = nextNodePtr;
	}

	TriplyNode<Data>* getPreviousNodePtr() {
		return previousNodePtr;
	}

	void setPreviousNodePtr(TriplyNode<Data>* previousNodePtr) {
		this->previousNodePtr = previousNodePtr;
	}
};
