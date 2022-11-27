#pragma once
#include <iostream>
#include <string>
using namespace std;

#include "Folder.h"
#include "File.h"

class Application {
private:
//	Folder* rootFolderPtr;
	//Folder* garbageFolderPtr;

//	Folder* currentFolderPtr;

//	Stack<Folder>* frontStackPtr;
//	Stack<Folder>* backStackPtr;

	// 바이너리파일 : 구조트리를 저장중임 add delete 하면 업데이트 : 문자열로 되어있음

public:
	Application();

	void init();

	void addFolder();

	void addFile();

	void deleteFolder();

	void deleteFile();

	void searchFolder();

	void searchFile();

	void openFolder();

	void openFile();

	void goBack();

	void goFront();

	void copyFolder();

	void copyFile();

	void cutAndPasteFolder();

	void cutAndPasteFile();

	void saveAll();

	void perfectDelete();

	void resetAll();

	void recovery();
};