#include "Application.h"

int main() {
	Application* app = new Application();
	app->init();

	Data<string>* d1 = new Data<string>("aaa", "Folder");
	Data<string>* d2 = new Data<string>("bcd", "Folder");
	Data<string>* d3 = new Data<string>("ced", "Folder");
	cout << d1->compare(d2) << endl;
	cout << d3->compare(d2) << endl;
	cout << d3->compare(d2) << endl;
}
