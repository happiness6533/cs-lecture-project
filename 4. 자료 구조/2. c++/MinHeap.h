#pragma once
#include "DoublyNode.h"

template <typename Data>
class MinHeap {
private:
	DoublyNode<Data>* headNodePtr;
	DoublyNode<Data>* currentNodePtr;
	int numOfNodes;

public:
	MinHeap() {
		numOfNodes = 0;
	}

	bool isEmpty() {
		if (numOfNodes == 0) {
			cout << "BST가 비어있습니다. " << endl;
			return true;
		}
		else {
			return false;
		}
	}

	void resetCurrentNodePtr() {
		if (isEmpty() == false) {
			currentNodePtr = headNodePtr;
		}
	}
};
