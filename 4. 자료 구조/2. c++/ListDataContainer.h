#pragma once
template <typename Data>
class ListDataContainer {
protected:
	virtual ~ListDataContainer() {}

	virtual bool isEmpty() = 0;
	virtual Data* searchData(Data* dataPtr) = 0;
	virtual bool addData(Data* dataPtr) = 0;
	virtual bool deleteData(Data* dataPtr) = 0;
	virtual void display() = 0;
};