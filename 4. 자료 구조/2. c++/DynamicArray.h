#pragma once
#include "ArrayDataContainer.h"
#include "SortAndSearch.h"

template <typename Data>
class DynamicArray : public ArrayDataContainer<Data> {
private:
	int IndexOfFinalDataPtr;
	int finalIndexOfDynamicArray;
	Data* dynamicArray[];

public:
	DynamicArray() {
		IndexOfFinalDataPtr = -1;
		finalIndexOfDynamicArray = 4;
		dynamicArray = new Data*[finalIndexOfDynamicArray + 1];
	}

	bool isEmpty() {
		if (IndexOfFinalDataPtr == -1) {
			return true;
		}
		else {
			return false;
		}
	}

	bool isFull() {
		if (IndexOfFinalDataPtr == finalIndexOfDynamicArray) {
			return true;
		}
		else {
			return false;
		}
	}

	int searchIndex(Data* dataPtr) {
		quickSort(0, IndexOfFinalDataPtr, dynamicArray);
		int resultIndex = binarySearch(0, IndexOfFinalDataPtr, dynamicArray, dataPtr);
		return resultIndex;
	}

	void addData(Data* dataPtr) {
		if (isEmpty()) {
			dynamicArray[IndexOfFinalDataPtr + 1] = dataPtr;
			IndexOfFinalDataPtr++;
			quickSort(0, IndexOfFinalDataPtr, dynamicArray);
			cout << "데이터 추가 성공. " << endl;
		}
		else if (isFull()) {
			int resultIndex = searchIndex(dataPtr);
			if (resultIndex == -1) {
				cout << "데이터 추가 실패 : 배열이 꽉 찼습니다. 배열의 크기를 확장시킵니다. " << endl;
				makeExpandDynamicArrray();
				dynamicArray[IndexOfFinalDataPtr + 1] = dataPtr;
				IndexOfFinalDataPtr++;
				quickSort(0, IndexOfFinalDataPtr, dynamicArray);
				cout << "데이터 추가 성공. " << endl;
			}
			else {
				cout << "데이터 추가 실패 : 배열에 데이터가 존재합니다. " << endl;
			}
		}
		else {
			int resultIndex = searchIndex(dataPtr);
			if (resultIndex == -1) {
				dynamicArray[IndexOfFinalDataPtr + 1] = dataPtr;
				IndexOfFinalDataPtr++;
				quickSort(0, IndexOfFinalDataPtr, dynamicArray);
				cout << "데이터 추가 성공. " << endl;
			}
			else {
				cout << "데이터 추가 실패 : 배열에 데이터가 존재합니다. " << endl;
			}
		}
	}

	void deleteData(Data* dataPtr) {
		if (isEmpty()) {
			cout << "데이터 삭제 실패 : 베열이 비어있습니다. " << endl;
		}
		else {
			int resultIndex = searchIndex(dataPtr);
			if (resultIndex != -1) {
				for (int i = resultIndex; i <= IndexOfFinalDataPtr - 1; i++) {
					dynamicArray[i] = dynamicArray[i + 1];
				}
				dynamicArray[IndexOfFinalDataPtr] = nullptr;
				IndexOfFinalDataPtr--;
				cout << "데이터 삭제 성공. " << endl;
			}
			else {
				cout << "데이터 삭제 실패 : 배열에 데이터가 존재하지 않습니다. " << endl;
			}
		}
	}

	void displayAll() {
		for (int i = 0; i <= IndexOfFinalDataPtr; i++) {
			if (i != IndexOfFinalDataPtr) {
				dynamicArray[i]->display();
			}
			else {
				dynamicArray[i]->display();
				cout << endl;
			}
		}
	}

	void makeExpandDynamicArrray() {
		Data* copyDynamicArrrayPtr[] = new Data*[finalIndexOfDynamicArray + 5];
		for (int i = 0; i <= IndexOfFinalDataPtr; i++) {
			copyDynamicArrrayPtr[i] = dynamicArray[i];
		}
		delete[] dynamicArray;
		dynamicArray = copyDynamicArrrayPtr;
	}
};