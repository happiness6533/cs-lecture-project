 #pragma once
#include "GraphNode.h"
#include "Stack.h"
#include "Queue.h"

template <typename Data ,typename Key>
class Graph {
private:
	int numOfNodes;
	GraphNode<Data, Key>** graphNodePtrList;

public:
	void setNodes(int numOfNodes, Data** dataPtrList) {
		this->numOfNodes = numOfNodes;
		graphNodePtrList = new GraphNode<Data, Key>*[numOfNodes];
		for (int i = 0; i < numOfNodes; i++) {
			GraphNode<Data, Key>* graphNodePtr = new GraphNode<Data, Key>(dataPtrList[i]);
			graphNodePtrList[i] = graphNodePtr;
		}
	}
	
	void setEdges(Data* dataPtr1, Data* dataPtr2) {
		for (int i = 0; i < numOfNodes; i++) {
			GraphNode<Data, Key>* graphNodePtr1 = graphNodePtrList[i];
			if (graphNodePtr1->getKey() == dataPtr1->getKey()) {
				for (int j = 0; j < numOfNodes; j++) {
					GraphNode<Data, Key>* graphNodePtr2 = graphNodePtrList[j];
					if (graphNodePtr2->getKey() == dataPtr2->getKey()) {
						cout << graphNodePtr1->getKey() << ", " << dataPtr1->getKey() << endl;
						cout << graphNodePtr2->getKey() << ", " << dataPtr2->getKey() << endl;
						graphNodePtr1->addAdjacentNode(graphNodePtr2);
					}					
				}
			}
		}
	}

	void resetVisitStatus() {
		for (int i = 0; i < numOfNodes; i++) {
			graphNodePtrList[i]->setVisitStatus(false);
		}
	}

	void dfsDisplayAndReset() {
		Stack<GraphNode<Data, Key>>* dfsStackPtr = new Stack<GraphNode<Data, Key>>();
		dfsStackPtr->push(graphNodePtrList[0]);
		graphNodePtrList[0]->setVisitStatus(true);// 스택에 들어가면 무조건 visit으로 한다?

		while(dfsStackPtr->isEmpty() != true) {
			GraphNode<Data, Key>* graphNodePtr = dfsStackPtr->pop();
			graphNodePtr->display();

			DoublyLinkedList<GraphNode<Data, Key>>* adjacentNodeList = graphNodePtr->getAdjacentNodeList();
			DoublyNode<GraphNode<Data, Key>>* adjacentCurrentNodePtr = adjacentNodeList->getHeadNodePtr();
			if (adjacentCurrentNodePtr != nullptr) {
				while (adjacentCurrentNodePtr->getNextNodePtr() != nullptr) {
					if (adjacentCurrentNodePtr->getDataPtr()->getVisitStatus() == false) {
						dfsStackPtr->push(adjacentCurrentNodePtr->getDataPtr());
						adjacentCurrentNodePtr->getDataPtr()->setVisitStatus(true);// 스택에 들어가면 무조건 visit으로 한다?
					}
					adjacentCurrentNodePtr = adjacentCurrentNodePtr->getNextNodePtr();
				}
				if (adjacentCurrentNodePtr->getDataPtr()->getVisitStatus() == false) {
					dfsStackPtr->push(adjacentCurrentNodePtr->getDataPtr());
					adjacentCurrentNodePtr->getDataPtr()->setVisitStatus(true); // 스택에 들어가면 무조건 visit으로 한다?
				}
			}
		}
		resetVisitStatus();
	}

	void dfsRecursiveDisplay(Data* dataPtr) {
		GraphNode<Data, Key>* currentGraphNodePtr = nullptr;
		for (int i = 0; i < numOfNodes; i++) {
			if (graphNodePtrList[i]->getKey() == dataPtr->getKey()) {
				currentGraphNodePtr = graphNodePtrList[i];
				currentGraphNodePtr->setVisitStatus(true);
				currentGraphNodePtr->display();
				break;
			}
		}
		DoublyLinkedList<GraphNode<Data, Key>>* adjacentNodeList = currentGraphNodePtr->getAdjacentNodeList();
		DoublyNode<GraphNode<Data, Key>>* adjacentCurrentNodePtr = adjacentNodeList->getHeadNodePtr();
		if (adjacentCurrentNodePtr != nullptr) {
			while (adjacentCurrentNodePtr->getNextNodePtr() != nullptr) {
				if (adjacentCurrentNodePtr->getDataPtr()->getVisitStatus() == false) {
					Data* dataPtr = adjacentCurrentNodePtr->getDataPtr()->getDataPtr();
					dfsRecursiveDisplay(dataPtr);
				}
				adjacentCurrentNodePtr = adjacentCurrentNodePtr->getNextNodePtr();
			}
			if (adjacentCurrentNodePtr->getDataPtr()->getVisitStatus() == false) {
				Data* dataPtr = adjacentCurrentNodePtr->getDataPtr()->getDataPtr();
				dfsRecursiveDisplay(dataPtr);
			}
		}
	}

	void dfsRecursiveDisplayAndReset(Data* dataPtr) {
		dfsRecursiveDisplay(dataPtr);
		resetVisitStatus();
	}

	void bfsDisplayAndReset() {
		Queue<GraphNode<Data, Key>>* bfsQueuePtr = new Queue<GraphNode<Data, Key>>();
		bfsQueuePtr->push(graphNodePtrList[0]);
		graphNodePtrList[0]->setVisitStatus(true); // 큐에 들어가면 무조건 visit으로 한다?


		while (bfsQueuePtr->isEmpty() != true) {
			GraphNode<Data, Key>* graphNodePtr = bfsQueuePtr->pop();
			graphNodePtr->display();

			DoublyLinkedList<GraphNode<Data, Key>>* adjacentNodeList = graphNodePtr->getAdjacentNodeList();
			DoublyNode<GraphNode<Data, Key>>* adjacentCurrentNodePtr = adjacentNodeList->getHeadNodePtr();
			if (adjacentCurrentNodePtr != nullptr) {
				while (adjacentCurrentNodePtr->getNextNodePtr() != nullptr) {
					if (adjacentCurrentNodePtr->getDataPtr()->getVisitStatus() == false) {
						bfsQueuePtr->push(adjacentCurrentNodePtr->getDataPtr());
						adjacentCurrentNodePtr->getDataPtr()->setVisitStatus(true);// 큐에 들어가면 무조건 visit으로 한다?
					}
					else {
						cout << "방문 이미 함" << endl;
					}
					adjacentCurrentNodePtr = adjacentCurrentNodePtr->getNextNodePtr();
				}
				if (adjacentCurrentNodePtr->getDataPtr()->getVisitStatus() == false) {
					bfsQueuePtr->push(adjacentCurrentNodePtr->getDataPtr());
					adjacentCurrentNodePtr->getDataPtr()->setVisitStatus(true);// 큐에 들어가면 무조건 visit으로 한다?
				}
			}
		}
		resetVisitStatus();
	}
};
