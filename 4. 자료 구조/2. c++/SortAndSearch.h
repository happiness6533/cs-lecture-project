#pragma once

template <typename Data>
int partition(int startIndex, int endIndex, Data* array[]) {
	int i = startIndex;
	int j = endIndex;
	int pivotIndex = (int)((i + j) / 2);
	Data* pivotDataPtr = array[pivotIndex];
	while (i <= j) {
		while (array[i]->compare(pivotDataPtr) < 0) {
			i++;
		}
		while (array[j]->compare(pivotDataPtr) > 0) {
			j--;
		}
		if (i <= j) {
			Data* tempDataPtr = array[i];
			array[i] = array[j];
			array[j] = tempDataPtr;
			i++;
			j--;
		}
	}
	return pivotIndex;
}

template <typename Data>
void quickSort(int startIndex, int endIndex, Data* array[]) {
	int partitionIndex = partition(startIndex, endIndex, array);
	if (startIndex <= partitionIndex - 1) {
		quickSort(startIndex, partitionIndex - 1, array);
	}
	if (partitionIndex + 1 <= endIndex) {
		quickSort(partitionIndex + 1, endIndex, array);
	}
}

template <typename Data>
int binarySearch(int startIndex, int endIndex, Data* array[], Data* targetDataPtr) {
	int i = startIndex;
	int j = endIndex;
	while (i <= j) {
		int middleIndex = (i + j) / 2;
		Data* middleDataPtr = array[middleIndex];
		if (middleDataPtr->compare(targetDataPtr) < 0) {
			i = middleIndex + 1;
		}
		else if (middleDataPtr->compare(targetDataPtr) > 0) {
			j = middleIndex - 1;
		}
		else {
			return middleIndex;
		}
	}
	return -1;
}
