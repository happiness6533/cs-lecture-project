#pragma once
#include "Iterator.h"
#include "SinglyNode.h"

// 왜 연산자 오버로딩이 안되는가?
template <typename Data>
class IteratorForSinglyLinkedList : public Iterator<Data> {
private:
	SinglyNode<Data>* startNodePtr;
	SinglyNode<Data>* endNodePtr;
	SinglyNode<Data>* currentNodePtr;

public:
	IteratorForSinglyLinkedList(SinglyNode<Data>* startNodePtr, SinglyNode<Data>* endNodePtr) {
		this->startNodePtr = startNodePtr;
		this->endNodePtr = endNodePtr;
		currentNodePtr = startNodePtr;
	}

	void getNext() {
		currentNodePtr = currentNodePtr->getNextNodePtr();
	}

	Data* getData() {
		return currentNodePtr->getDataPtr();
	}

	bool hasNext() {
		if (currentNodePtr->getNextNodePtr() != endNodePtr) {
			return true;
		}
		else {
			return false;
		}
	}
};
