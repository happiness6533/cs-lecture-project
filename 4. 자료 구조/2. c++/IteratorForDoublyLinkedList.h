#pragma once
#include "Iterator.h"
#include "DoublyNode.h"

template <typename Data>
class IteratorForDoublyLinkedList : public Iterator<Data> {
private:
	DoublyNode<Data>* startNodePtr;
	DoublyNode<Data>* endNodePtr;
	DoublyNode<Data>* currentNodePtr;

public:
	IteratorForDoublyLinkedList(DoublyNode<Data>* startNodePtr, DoublyNode<Data>* endNodePtr) {
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
