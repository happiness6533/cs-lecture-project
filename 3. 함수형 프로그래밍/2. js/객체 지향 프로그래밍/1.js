// 객체 지향 프로그래밍이 가능한 언어들은 크게 2가지 종류

// 첫 번째는 클래스 기반의 객체 지향 언어,
// 두 번째는 프로토타입 기반의 객체 지향 언어
// 대표적인, 클래스 기반의 객체 지향 언어로 Java
// 대표적인 프로토타입 기반의 객체 지향 언어로 JavaScript

// 객체 만들기

// 1. Object literal
const user = {
    email: "a",
    show() {
        console.log(this.email);
    }
}

// 2. Factory function
const createUser = (email) => {
    return {
        email,
        show() {
            console.log(this.email);
        }
    }
}

// 3. Constructor function
const User = (email) => {
    this.email = email;
    this.show = () => {
        console.log(this.email);
    }
}
const user1 = new User("asdasd");

// 4. 클래스
class User {
    constructor(email) {
        this.email = email;
    }

    show() {
        console.log(this.email)
    }
}