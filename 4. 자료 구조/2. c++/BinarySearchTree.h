#pragma once
#include "TriplyNode.h"

template <typename Data>
class BinarySearchTree {
private:
	TriplyNode<Data>* headNodePtr;
	TriplyNode<Data>* currentNodePtr;
	TriplyNode<Data>* tempNodePtr;
	int leftOrRight;
	int numOfNodes;

public:
	BinarySearchTree() {
		numOfNodes = 0;
		tempNodePtr = nullptr;
		leftOrRight = 0;
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

	Data* searchData(Data* dataPtr) {
		if(numOfNodes == 0) {
			cout << "BST가 비어있습니다. " << endl;
			return nullptr;
		}

		resetCurrentNodePtr();
		while (currentNodePtr->getPreviousNodePtr() != nullptr || currentNodePtr->getNextNodePtr() != nullptr) {
			if (currentNodePtr->getDataPtr()->compare(dataPtr) > 0) {
				tempNodePtr = currentNodePtr;
				leftOrRight = -1;
				if (currentNodePtr->getPreviousNodePtr() == nullptr) {
					cout << "데이터가 존재하지 않습니다" << endl;
					return nullptr;
				}
				currentNodePtr = currentNodePtr->getPreviousNodePtr();
			}
			else if (currentNodePtr->getDataPtr()->compare(dataPtr) < 0) {
				tempNodePtr = currentNodePtr;
				leftOrRight = 1;
				if (currentNodePtr->getNextNodePtr() == nullptr) {
					cout << "데이터가 존재하지 않습니다" << endl;
					return nullptr;
				}
				currentNodePtr = currentNodePtr->getNextNodePtr();
			}
			else {
				return currentNodePtr->getDataPtr();
			}
		}
		if (currentNodePtr->getDataPtr()->compare(dataPtr) == 0) {
			return currentNodePtr->getDataPtr();
		}
		cout << "데이터가 존재하지 않습니다" << endl;
		return nullptr;
	}

	bool addData(Data* dataPtr) {
		if (numOfNodes == 0) {
			headNodePtr = new TriplyNode<Data>(dataPtr);
			currentNodePtr = headNodePtr;
			numOfNodes++;
			cout << "데이터를 추가합니다. " << endl;
			return true;
		}

		resetCurrentNodePtr();
		Data* searchResult = searchData(dataPtr);
		if (searchResult == nullptr) {
			TriplyNode<Data>* addNodePtr = new TriplyNode<Data>(dataPtr);
			if (currentNodePtr->getDataPtr()->compare(dataPtr) > 0) {
				currentNodePtr->setPreviousNodePtr(addNodePtr);
				addNodePtr->setMotherNodePtr(currentNodePtr);
			}
			else if (currentNodePtr->getDataPtr()->compare(dataPtr) < 0) {
				currentNodePtr->setNextNodePtr(addNodePtr);
				addNodePtr->setMotherNodePtr(currentNodePtr);
			}
			numOfNodes++;
			return true;
		}
		else {
			cout << "데이터가 이미 존재합니다. " << endl;
			return false;
		}
	}

	bool deleteData(Data* dataPtr) {
		if (numOfNodes == 0) {
			cout << "BST가 비어있습니다. " << endl;
			return false;
		}

		resetCurrentNodePtr();
		Data* searchResult = searchData(dataPtr);
		if (searchResult == nullptr) {
			cout << "데이터가 존재하지 않습니다. " << endl;
			return false;
		}
		else {
			// 루트는 따로 처리하자
			if (currentNodePtr->getMotherNodePtr() == nullptr) {
				delete currentNodePtr;
				numOfNodes = 0;
				tempNodePtr = nullptr;
				leftOrRight = 0;
				return true;
			}

			if (currentNodePtr->getPreviousNodePtr() == nullptr && currentNodePtr->getNextNodePtr() == nullptr) {
				if (leftOrRight == -1) {
					currentNodePtr->getMotherNodePtr()->setPreviousNodePtr(nullptr);
				}
				else {
					currentNodePtr->getMotherNodePtr()->setNextNodePtr(nullptr);
				}
				delete currentNodePtr;
			}
			else if (currentNodePtr->getPreviousNodePtr() != nullptr && currentNodePtr->getNextNodePtr() == nullptr){
				if (leftOrRight == -1) {
					currentNodePtr->getMotherNodePtr()->setPreviousNodePtr(currentNodePtr->getPreviousNodePtr());
					currentNodePtr->getPreviousNodePtr()->setMotherNodePtr(currentNodePtr->getMotherNodePtr());
				}
				else {
					currentNodePtr->getMotherNodePtr()->setNextNodePtr(currentNodePtr->getPreviousNodePtr());
					currentNodePtr->getPreviousNodePtr()->setMotherNodePtr(currentNodePtr->getMotherNodePtr());
				}
				delete currentNodePtr;
			}
			else if (currentNodePtr->getPreviousNodePtr() == nullptr && currentNodePtr->getNextNodePtr() != nullptr) {
				if (leftOrRight == -1) {
					currentNodePtr->getMotherNodePtr()->setPreviousNodePtr(currentNodePtr->getNextNodePtr());
					currentNodePtr->getNextNodePtr()->setMotherNodePtr(currentNodePtr->getMotherNodePtr());
				}
				else {
					currentNodePtr->getMotherNodePtr()->setNextNodePtr(currentNodePtr->getNextNodePtr());
					currentNodePtr->getNextNodePtr()->setMotherNodePtr(currentNodePtr->getMotherNodePtr());
				}
				delete currentNodePtr;
			}
			else {
				TriplyNode<Data>* parentNodePtr0fCandidateNodePtr;
				TriplyNode<Data>* candidateNodePtr;

				candidateNodePtr = currentNodePtr->getNextNodePtr();
				if (candidateNodePtr->getPreviousNodePtr() != nullptr) {
					while (candidateNodePtr->getPreviousNodePtr() != nullptr) {
						candidateNodePtr = candidateNodePtr->getPreviousNodePtr();
					}
					currentNodePtr->setDataPtr(candidateNodePtr->getDataPtr());
					candidateNodePtr->getMotherNodePtr()->setPreviousNodePtr(nullptr);
					delete candidateNodePtr;
				}
				else {
					currentNodePtr->setDataPtr(candidateNodePtr->getDataPtr());
					if (candidateNodePtr->getNextNodePtr() != nullptr) {
						currentNodePtr->setNextNodePtr(candidateNodePtr->getNextNodePtr());
						candidateNodePtr->getNextNodePtr()->setMotherNodePtr(currentNodePtr);
					}
					else {
						currentNodePtr->setNextNodePtr(nullptr);
					}
					delete candidateNodePtr;
				}
			}
			numOfNodes--;
			return true;
		}
	}

	void preOrder(TriplyNode<Data>* currentNodePtr) {
		if (currentNodePtr->getPreviousNodePtr() != nullptr && currentNodePtr->getNextNodePtr() != nullptr) {
			currentNodePtr->getDataPtr()->display();
			preOrder(currentNodePtr->getPreviousNodePtr());
			preOrder(currentNodePtr->getNextNodePtr());
		}
		else if (currentNodePtr->getPreviousNodePtr() != nullptr && currentNodePtr->getNextNodePtr() == nullptr) {
			currentNodePtr->getDataPtr()->display();
			preOrder(currentNodePtr->getPreviousNodePtr());
		}
		else if (currentNodePtr->getPreviousNodePtr() == nullptr && currentNodePtr->getNextNodePtr() != nullptr) {
			currentNodePtr->getDataPtr()->display();
			preOrder(currentNodePtr->getNextNodePtr());
		}
		else {
			currentNodePtr->getDataPtr()->display();
		}
	}

	void display() {
		if (numOfNodes == 0) {
			cout << "BST가 비어있습니다" << endl;
		}
		else {
			resetCurrentNodePtr();
			preOrder(currentNodePtr);
		}
		cout << endl;
	}
};
