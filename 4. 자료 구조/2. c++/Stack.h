#pragma once
#include "SinglyNode.h"

template <typename Data>
class Stack {
private:
	DoublyNode<Data>* bottomNodePtr;
	DoublyNode<Data>* topNodePtr;
	int numOfNodes;
	int maxNumOfNodes;
public:
	Stack() {
		numOfNodes = 0;
		maxNumOfNodes = 1000;
	}

	void push(Data* dataPtr) {
		if (numOfNodes == 0) {
			bottomNodePtr = new DoublyNode<Data>(dataPtr);
			topNodePtr = bottomNodePtr;
		}
		else if (numOfNodes == maxNumOfNodes) {
			cout << "stack overflow" << endl;
		}
		else {
			DoublyNode<Data>* addNodePtr = new DoublyNode<Data>(dataPtr);
			topNodePtr->setNextNodePtr(addNodePtr);
			addNodePtr->setPreviousNodePtr(topNodePtr);
			topNodePtr = addNodePtr;
		}
		numOfNodes++;
	}

	Data* pop() {
		if (numOfNodes >= 2) {
			DoublyNode<Data>* candidateTopNodePtr = topNodePtr->getPreviousNodePtr();
			Data* topDataPtr = topNodePtr->getDataPtr();

			topNodePtr->getPreviousNodePtr()->setNextNodePtr(nullptr);
			delete topNodePtr;
			topNodePtr = candidateTopNodePtr;
			numOfNodes--;

			return topDataPtr;
		}
		else if (numOfNodes == 1) {
			Data* topDataPtr = topNodePtr->getDataPtr();
			delete topNodePtr;
			numOfNodes--;
			return topDataPtr;
		}
		else {
			cout << "stack이 비었습니다" << endl;
			return nullptr;
		}

	}

	void peek() {
		topNodePtr->getDataPtr()->display();
	}

	bool isEmpty() {
		if (numOfNodes == 0) {
			return true;
		}
		else {
			return false;
		}
	}
};
