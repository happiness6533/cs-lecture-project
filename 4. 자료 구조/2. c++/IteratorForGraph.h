#pragma once
template <typename Data>
class prac {
private:
	int size = 5;
	Data* arr = new Data[size];
	int count;
public:
	int* getArray() {
		return arr;
	}

	void add(int a) {
		if (count <= size) {
			arr[count] = a;
			count++;
		}
		else {
			size += 5;
			int* temp = new int[size];
			for (int i = 0; i < 5; i++) {
				temp[i] = arr[i];
			}
			delete[] arr;
			arr = temp;
		}

	}

};