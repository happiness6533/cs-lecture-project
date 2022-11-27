#pragma once
#include "Iterator.h"
// 문제 2개 해결해야 한다
// 왜 연산자 오버로딩이 안되는가?
template <typename Data>
class IteratorForArray : public Iterator<Data>{
private:
	Data** startPtr;
	Data** endPtr;
	Data** currentPtr;

public:
	IteratorForArray(Data** startPtr, Data** endPtr) {
		this->startPtr = startPtr;
		this->endPtr = endPtr;
		currentPtr = startPtr;
	}

	void getNext() {
		this->currentPtr += 1;
	}

	Data* getData() {
		return *(this->currentPtr);
	}

	bool hasNext() {
		if (this->currentPtr + 1 != this->endPtr) {
			return true;
		}
		else {
			return false;
		}
	}
};
