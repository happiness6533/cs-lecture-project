#pragma once

template <typename Data>
class Iterator {
public:
	virtual ~Iterator() {}

	virtual void getNext() = 0;

	virtual Data* getData() = 0;

	virtual bool hasNext() = 0;
};
