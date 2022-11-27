#pragma once
#include "ListDataContainer.h"
#include "DoublyNode.h"
#include "IteratorForDoublyLinkedList.h"

template <typename Data>
class DoublyLinkedList : public ListDataContainer<Data> {
private:
	DoublyNode<Data>* headNodePtr;
	DoublyNode<Data>* currentNodePtr;
	int numOfNodes;

public:
	DoublyLinkedList() {
		numOfNodes = 0;
	}

	bool isEmpty() {
		if (numOfNodes == 0) {
			cout << "더블리 링크드리스트가 비어있습니다. " << endl;
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
			cout << "더블리 링크드리스트가 비어있습니다. " << endl;
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
			headNodePtr = new DoublyNode<Data>(dataPtr);
			currentNodePtr = headNodePtr;
			numOfNodes++;
			cout << "데이터를 추가합니다. " << endl;
			return true;
		}

		resetCurrentNodePtr();
		Data* searchResult = searchData(dataPtr);
		if (searchResult == nullptr) {
			DoublyNode<Data>* addNodePtr = new DoublyNode<Data>(dataPtr);
			currentNodePtr->setNextNodePtr(addNodePtr);
			addNodePtr->setPreviousNodePtr(currentNodePtr);
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
			cout << "더블리 링크드리스트가 비어있습니다. " << endl;
			return false;
		}

		resetCurrentNodePtr();
		Data* searchResult = searchData(dataPtr);
		if (searchResult == nullptr) {
			cout << "데이터가 존재하지 않습니다. " << endl;
			return false;
		}
		else {
			currentNodePtr->getPreviousNodePtr()->setNextNodePtr(currentNodePtr->getNextNodePtr());
			currentNodePtr->getNextNodePtr()->setPreviousNodePtr(currentNodePtr->getPreviousNodePtr());
			delete currentNodePtr;
			return true;
		}
	}

	void display() {
		if (numOfNodes == 0) {
			cout << "더블리 링크드리스트가 비어있습니다. " << endl;
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

	DoublyNode<Data>* getHeadNodePtr() { // 반복자를 구현하고 이 메소드는 삭제한다
		if (numOfNodes != 0) {
			return headNodePtr;
		}
		else {
			return nullptr;
		}
	}

	Iterator<Data>* makeIterator() {
		resetCurrentNodePtr();
		while (currentNodePtr->getNextNodePtr() != nullptr) {
			currentNodePtr = currentNodePtr->getNextNodePtr();
		}
		currentNodePtr = currentNodePtr->getNextNodePtr();
		Iterator<Data>* iterator = new IteratorForDoublyLinkedList<Data>(headNodePtr, currentNodePtr);
		return iterator;
	}
};
