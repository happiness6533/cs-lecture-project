#pragma once
#include "ListDataContainer.h"
#include "SinglyNode.h"
#include "IteratorForSinglyLinkedList.h"

template <typename Data>
class SinglyLinkedList : public ListDataContainer<Data> {
private:
	SinglyNode<Data>* headNodePtr;
	SinglyNode<Data>* currentNodePtr;
	int numOfNodes;
	
public:
	SinglyLinkedList() {
		numOfNodes = 0;
	}

	bool isEmpty() {
		if (numOfNodes == 0) {
			cout << "싱글리 링크드리스트가 비어있습니다. " << endl;
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
		if (numOfNodes == 0) {
			cout << "링크드리스트가 비어있습니다" << endl;
			return nullptr;
		} 

		resetCurrentNodePtr();
		while (currentNodePtr->getNextNodePtr() != nullptr) {
			if (dataPtr->getKey() == currentNodePtr->getDataPtr()->getKey()) {
				cout << "데이터가 존재합니다" << endl;
				return dataPtr;
			}
			else {
				currentNodePtr = currentNodePtr->getNextNodePtr();
			}
		}
		cout << "데이터가 존재하지 않습니다" << endl;
		return nullptr;
	}

	bool addData(Data* dataPtr) {
		if (numOfNodes == 0) {
			headNodePtr = new SinglyNode<Data>(dataPtr);
			currentNodePtr = headNodePtr;
			numOfNodes++;
			return true;
		}

		resetCurrentNodePtr();
		Data* searchResult = searchData(dataPtr);
		if (searchResult == nullptr) {
			SinglyNode<Data>* addNode = new SinglyNode<Data>(dataPtr);
			currentNodePtr->setNextNodePtr(addNode);
			return true;
		}
		else {
			cout << "데이터가 이미 존재한다" << endl;
			return false;
		}
	}
	
	bool deleteData(Data* dataPtr) {
		if (numOfNodes == 0) {
			cout << "링크드리스트가 비어있습니다" << endl;
			return false;
		}

		resetCurrentNodePtr();
		Data* searchResult = searchData(dataPtr);
		if (searchResult == nullptr) {
			cout << "삭제할 데이터는 존재하지 않는다" << endl;
			return false;
		}
		else {
			Data* tempDataPtr = currentNodePtr->getNextNodePtr()->getDataPtr();
			SinglyNode<Data>* tempNodePtr = currentNodePtr->getNextNodePtr()->getNextNodePtr();

			delete currentNodePtr->getDataPtr();
			currentNodePtr->setDataPtr(tempDataPtr);

			delete currentNodePtr->getNextNodePtr();
			currentNodePtr->setNextNodePtr(tempNodePtr);
			return true;
		}
	}

	void display() {
		if (numOfNodes == 0) {
			cout << "링크드리스트가 비어있습니다" << endl;
		}
		else {
			resetCurrentNodePtr();
			while (currentNodePtr->getNextNodePtr() != nullptr) {
				currentNodePtr->getDataPtr()->display();
				currentNodePtr = currentNodePtr->getNextNodePtr();
			}
			currentNodePtr->getDataPtr()->display();
		}
	}

	Iterator<Data>* makeIterator() {
		resetCurrentNodePtr();
		while (currentNodePtr->getNextNodePtr() != nullptr) {
			currentNodePtr = currentNodePtr->getNextNodePtr();
		}
		currentNodePtr = currentNodePtr->getNextNodePtr();
		Iterator<Data>* iterator = new IteratorForSinglyLinkedList<Data>(headNodePtr, currentNodePtr);
		return iterator;
	}	
};
