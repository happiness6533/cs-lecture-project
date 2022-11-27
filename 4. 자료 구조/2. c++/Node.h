#pragma once
template <typename Data>
class Node {
protected:
	Data* dataPtr;

public:
	Node(Data* dataPtr) {
		this->dataPtr = dataPtr;
	}
	virtual ~Node() {}
	
	Data* getDataPtr() {
		return dataPtr;
	}

	void setDataPtr(Data* dataPtr) {
		this->dataPtr = dataPtr;
	}
};
