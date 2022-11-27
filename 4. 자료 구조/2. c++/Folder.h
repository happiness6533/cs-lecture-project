#pragma once
#include "Data.h"
#include <string.h>
#include "BinarySearchTree.h"

class Folder : public Data<string> {
private:
	string nameOfFolder;
	BinarySearchTree<Data<string>>* datas;
public:
	Folder(string nameOfFolder, string tag) : Data(nameOfFolder, tag) {
		this->nameOfFolder = nameOfFolder;
		datas = new BinarySearchTree<Data<string>>();
	}

	bool isEmpty() {
		if (datas->isEmpty()) {
			return true;
		}
		else {
			return false;
		}
	}

	bool addFolder(string nameOfFolder) {
		Data<string>* dummyFolder = new Folder(nameOfFolder, "Folder");
		return datas->addData(dummyFolder);
	}

	bool deleteFolder(string nameOfFolder) {
		Data<string>* dummyFolder = new Folder(nameOfFolder, "Folder");
		return datas->deleteData(dummyFolder);
	}

	Folder* searchFolder(string nameOfFolder) {
		Data<string>* dummyFolder = new Folder(nameOfFolder, "Folder");
		Folder* resultOfSearch = (Folder*) (datas->searchData(dummyFolder));
		if (resultOfSearch != nullptr) {
			return resultOfSearch;
		}
		else {
			// 반복자를 돌면서 각 노드마다 순회하면서 search를 재귀적으로 적용해야 함
			return nullptr;
		}
	}

	void display() {
		datas->display();
	}
};