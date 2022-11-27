#pragma once

#include "Data.h"
#include <string.h>
#include "BinarySearchTree.h"

class File : public Data<string> {
private:
	string nameOfFile;
	string extName;
	char* content;

public:
	File(string nameOfFile, string tag) : Data(nameOfFile, tag) {
		this->nameOfFile = nameOfFile;
	}

	void readFile() {
		// 바이너리 배열 콘텐츠를 읽어서 콘솔에 텍스트로 출력
	}

	bool saveFile() {

	}

	bool changeFileOfContent() {

	}

	bool changeFileOfName() {

	}
};