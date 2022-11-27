#include "Application.h"

Application::Application() {

}

void Application::init() {

}

void Application::addFolder() {

}

void Application::addFile() {

}

void Application::deleteFolder() {
	// 진짜 delete 폴더 구현하지 않고, cutAndPaste 구현
}

void Application::deleteFile() {

}

void Application::searchFolder() {
	// 내부 전부 다 검사
}

void Application::searchFile() {
	// 내부 전부 다 검사
	// 이걸 간단하게 하도록 도와주는 바이너리 구조트리가 있으면 편리함
}
void Application::openFolder() {

}

void Application::openFile() {

}

void Application::goBack() {

}

void Application::goFront() {

}

void Application::copyFolder() {
	// 내부 깊은 복사	
	// 바이너리 파일을 사용하기
}

void Application::copyFile() {
	// 내부 깊은 복사	
	// 바이너리 파일을 사용하기
}

void Application::cutAndPasteFolder() {
	// 얕은 복사로 포인터를 가져와서
	// 포인터의 존재 위치를 변경
}

void Application::cutAndPasteFile() {
	// 얕은 복사로 포인터를 가져와서
	// 포인터의 존재 위치를 변경
}

void Application::saveAll() {
	// 바이너리 파일로 저장
}

void Application::perfectDelete() {
	// 휴지통 내부의 포인터 delete
}

void Application::recovery() {
	// 휴지통 내부의 포인터들을 원래 위치로 되돌림
}

void Application::resetAll() {
	// 모든 포인터를 delete
}