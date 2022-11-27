#pragma once

template <typename Key>
class Data {
private:
	Key key;
	string tag;

public: // 데이터를 상속받는 실제 데이터 클래스를 작성하면 부모 데이터의 메소드는 프로텍티드로 변경한다
	Data(Key key, string tag) {
		this->key = key;
		this->tag = tag;
	}
	virtual ~Data() {};

	Key getKey() {
		return key;
	}

	int compare(Data* dataPtr2) {
		if (typeid(Key) == typeid(int)) {
			if (key < dataPtr2->key) {
				return -1;
			}
			else if (key == dataPtr2->key){
				if (tag == dataPtr2->tag) {
					return 0;
				}
				else if (tag == "Folder") {
					return 1;
				}
				else {
					return -1;
				}
			}
			else {
				return 1;
			}
		} else if (typeid(Key) == typeid(string)) {
			if (key.compare(dataPtr2->key) < 0) {
				return -1;
			}
			else if (key.compare(dataPtr2->key) == 0) {
				if (tag == dataPtr2->tag) {
					return 0;
				}
				else if (tag == "Folder") {
					return 1;
				}
				else {
					return -1;
				}
			}
			else {
				return 1;
			}
		}
		else {
			cout << "compare 메소드를 사용하기 위한 Key의 자료형은 int, char, string으로 제한됩니다. " << endl;
		}
	}

	virtual void display() {
		cout << key << endl;
	}
};