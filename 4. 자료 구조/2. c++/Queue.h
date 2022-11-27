#pragma once
#include "DoublyNode.h"

template <typename Data>
class Queue {
private:
	DoublyNode<Data>* headNodePtr;
	DoublyNode<Data>* tailNodePtr;
	int numOfNodes;


public:
	Queue () {
		numOfNodes = 0;
		headNodePtr = nullptr;
		tailNodePtr = headNodePtr;
	}

	void push(Data* dataPtr) {
		if (numOfNodes == 0) {
			headNodePtr = new DoublyNode<Data>(dataPtr);
			tailNodePtr = headNodePtr;
		}
		else {
			DoublyNode<Data>* addNodePtr = new DoublyNode<Data>(dataPtr);
			tailNodePtr->setNextNodePtr(addNodePtr);
			addNodePtr->setPreviousNodePtr(tailNodePtr);
			tailNodePtr = addNodePtr;
		}
		numOfNodes++;
	}

	Data* pop() {
		if (numOfNodes >= 2) {
			DoublyNode<Data>* candidateHeadNodePtr = headNodePtr->getNextNodePtr();
			Data* headDataPtr = headNodePtr->getDataPtr();

			headNodePtr->getNextNodePtr()->setPreviousNodePtr(nullptr);
			delete headNodePtr;
			headNodePtr = candidateHeadNodePtr;
			numOfNodes--;

			return headDataPtr;
		}
		else if (numOfNodes == 1) {
			Data* headDataPtr = headNodePtr->getDataPtr();
			delete headNodePtr;
			numOfNodes--;
			return headDataPtr;
		}
		else {
			cout << "Queue가 비었습니다" << endl;
			return nullptr;
		}

	}

	void peek() {
		if (numOfNodes != 0) {
			headNodePtr->getDataPtr()->display();
		}
		else {
			cout << "Queue가 비었습니다" << endl;
		}
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