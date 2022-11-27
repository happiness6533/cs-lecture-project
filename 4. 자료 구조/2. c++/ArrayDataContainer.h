#pragma once
#include "IteratorForArray.h"

template <typename Data>
class ArrayDataContainer {
protected:
	virtual ~ArrayDataContainer() {}

	virtual bool isEmpty() = 0;
	virtual bool isFull() = 0;
	virtual int searchIndex(Data* dataPtr) = 0;
	virtual void addData(Data* dataPtr) = 0;
	virtual void deleteData(Data* dataPtr) = 0;
	virtual void displayAll() = 0;
};
