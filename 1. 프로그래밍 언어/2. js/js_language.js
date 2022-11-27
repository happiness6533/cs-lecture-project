// 자바스크립트


// 1. 자바스크립트란?
// 자바스크립트는 객체들의 집합이다
// 자바스크립트는 크롬의 v8 엔진(인터프리터)을 사용해서 브라우저와 노드, 2가지 환경에서 동작한다
// 브라우저 환경의 전역객체: window 객체
// 노드 환경의 전역객체: global 객체


// 2. 변수
// let, const, var(더 이상 사용되지 않는다)


// 3. 자료형과 연산자
// 프리미티브 타입: Number, String, Boolean, null, undefined, symbol: 값을 참조한다
// 레퍼런스 타입: 객체: 주소를 참조한다
// 문자열 포멧팅: 백틱: `문자열${자바스크립트 변수}문자열`
// 등호 연산자: ===, !==
// 전개 연산자
const a = [1, 2];
const b = new Set([3, [4, 5]]);
const c = new Map([['x', 1], ['y', 2]]);
const total = [...a, ...b, ...c.keys(), ...c.values(), ...c.entries()];
const [head, ...rest] = total;
console.log(total);
console.log(head);
console.log(rest);


// 4. 제어문
// 여러 비동기의 순서를 제어할 수 있어야 한다: 자바스크립트 비동기 파트에서 다룬다
// 여러 비동기를 병렬로 제어할 수 있어야 한다: 자바스크립트 함수형 프로그래밍에서 다룬다


// 5. 입출력
// 브라우저 환경: window 객체의 console.log, console.error, alert, prompt, document.write
// 노드 환경: global 객체의 console.log, console.error


// 6. 객체 표기법
// 기본 표기법
let obj1 = new Number(1);
let obj2 = new String('hello');
let obj3 = new Boolean(true);
let obj4 = new Array();
let obj5 = new Object();

// 단순 표기법 = json 표기법
let obj6 = 1;
let obj7 = 'hello';
let obj8 = true;
let obj9 = [1, '2', true];
let func2 = function () {
    console.log('hello world');
};
let x2 = 'hello ';
let obj10 = { // key = 문자열
    'name': '김성주',
    age: 25,
    'skill set': {
        math: 'lv7',
        magic: 'lv8',
        programming: 'lv6'
    },
    func1() { // 키-값이 함수인 경우 이렇게 축약
        console.log('hello world');
    },
    func2, // 키-값이 동일한 경우 이렇게 축약
    [x2 + 'world']: '객체의 키에 변수가 들어있는 경우 이렇게 처리'
};
console.log(obj10['skill set']);

// json 다루기
// json -> 문자열: JSON.stringify(json);
// 문자열 -> json: JSON.parse(문자열);
let stringObj10 = JSON.stringify(obj10);
let obj10Copy = JSON.parse(stringObj10);


// 7. 객체
// 순서대로 읽으면 이해할 수 있습니다

// 자바스크립트는 객체의 집합이다
// // 모든 객체는 함수로 생성한다
// // 따라서 모든 객체는 자신을 생성한 함수가 존재한다
//
// // 함수를 정의하면 2가지 객체가 생성된다
// // 함수를 정의해서 생성된 객체1: 함수 객체: prototype(바로 아래의 프로토타입 객체를 가르키는 링크)을 내부에 가지고 있다
// // 함수를 정의해서 생성된 객체2: 함수 객체의 프로토타입 객체: 생성자를 내부에 가지고 있다, __proto__(이게 뭔지 아래에 설명)를 가지고 있다
//
// // 위의 설명을 이해하면 아래의 설명을 이해할 수 있습니다
//
// // 모든 객체는 함수로 생성한다
// // 따라서 모든 객체는 자신을 생성한 함수가 존재한다
// // 함수를 정의하면 2가지 객체가 생성된다: 그 중에서 함수를 정의해서 생성된 객체2, 즉 함수 객체의 프로토타입 객체가 생성된다
// // 따라서 다음의 연결 관계가 성립한다
// // 생성한 객체 >> 객체 자신을 생성한 함수 >> 그 함수의 프로토타입 객체
// // 이 때, 제일 앞과 뒤의 연결, 즉 객체와, 그 객체를 생성한 함수의 프로토타입 객체의 연결이 있을 수 있다
// // 자바스크립트의 모든 객체는, 이 링크를 가지고 았으며 그 링크의 이름은 __proto__

let protoCharacter = { // 부모 역할을 할 객체를 하나 만들었다
    type: 'wizard',
    fireBall: function () {
        console.log('fire ball');
    }
};

// 객체 생성1: 사용x
function characterFactory1(name) {
    let character = { // 객체 하나를 만들었다
        name: name
    };
    character.__proto__ = protoCharacter; // 객체를 생성한 함수의 프로토타입 객체를 결정했다
    return character;
}

// 객체 생성2: 위를 간략화한 것이다. 사용x
function characterFactory2(name) {
    let character = Object.create(protoCharacter);
    character.name = name;

    return character;
}

// 객체 생성3: 사용o
function CharacterFactory3(name) { // 객체를 생성할 함수를 정의한다
    this.name = name; // 이 함수로 객체를 만들면 이 속성을 복사해서 가진다
    this.waterBall = () => { // 이 함수로 객체를 만들면 이 속성을 복사해서 가진다
        console.log('water ball 특정 객체만 사용할 메소드 추가는 이렇게')
    }
}

CharacterFactory3.prototype = protoCharacter; // 함수의 프로토타입 객체를 내가 원하는 객체로 세팅한다
CharacterFactory3.prototype.fireBall = () => { // 함수의 프로토타입 객체에 내가 원하는 메소드를 세팅한다
    console.log('fire ball 메소드 오버라이딩은 이렇게')
};
let character1 = new CharacterFactory3('김성주'); // 객체를 생성한다
character1.fireBall(); // 생성된 객체는 __proto__ 링크에 의해 함수의 프로토타입 객체 내부를 참조해서 메소드를 사용한다
character1.waterBall(); // 생성된 객체는 현재 객체 내부를 참조해서 메소드를 사용한다
// 위와 같이 객체는 일단 자신 내부의 데이터 또는 메소드를 찾고(waterBall()),
// 찾는 결과가 없는 경우 __proto__ 속성을 통해 계속해서 자신을 생성한 함수의 프로토타입 객체를 찾아가서 데이터 또는 메소드를 찾는다(fireBall())
// 이러한 내부 검색 방식을 프로토타입 체인이라고 한다
// 헷갈리면 character1을 콘솔에 직접 찍어보고 내부를 확인한다


// 8. 배열 객체
// 이질리스트, [], length, push, pop, unshift, shift
// splice(2, 3): 2번 인덱스에서 시작, 3개의 원소를 선택 후 배열로 리턴, 배열에서 해당 원소들은 제거
// splice(2, 0, 3) : 2번 인덱스에서 시작, 3을 배열에 삽입
// forEach(callback), indexOf, contains, sort(callback), join, split


// 9. 함수 객체
// 함수1: 일급 객체다: 객체이며, 변수에 담겨서, 다른 함수의 파라미터로 사용된다: 자바스크립트 함수형 프로그래밍에서 다룬다
// 함수2: call by value
// 함수3: 스코프 체인과 클로저
let closureExampleFunction = function () {
    let c = 1;
    return closureFunction = function () {
        let b = c + 1; // 위의 리턴에 의해 closureFunction 함수가 리턴되었지만, 데이터 c는 여전히 스택에 남아서 closureFunction에 의해 기억된다
        // 이러한 데이터와 함수의 관계를 클로저 관계라고 하며, 특정 데이터를 기억하고 있는 함수를 클로저 함수라고 한다
        // 이렇게 현재 리턴된 함수 내부에 데이터가 없는 경우, 함수는 그 함수를 감싸고 있는 상위 스코프(범위)에서 해당 데이터를 검색하는데, 이를 스코프 체인이라고 한다
        return b;
    };
};
let closure = closureExampleFunction();
console.log(closure());

// 함수4: 화살표 함수
let func3 = (a, b) => {
    return a + b;
};
let func4 = (a, b) => a + b; // 리턴만 사용하는 경우 중괄호와 return 생략
// 화살표 함수는 this가 존재하지 않기 때문에, 스코프 체인에 의해 상위 스코프의 this가 화살표 함수의 this

// 함수5: this
// this = this가 들어있는 함수를 호출한 객체
// 일반 함수에서 this -> window
// 메소드에서 this -> 객체
// 이벤트 핸들러에서 this -> 돔 객체
// 객체1.메소드.bind(객체2): 객체1 메소드의 this를 객체2로 변환
// 객체1.prototype.메소드.call(객체2, 메소드에 필요한 파라미터): 객체1 메소드의 this를 객체2로 임시 변환: 객체2가 객체1의 메소드를 사용할 수 있다


// 함수5: 파라미터에 활용되는 전개 연산자
let func5 = (x5, ...rest) => {
    console.log(x5, rest);
};
func5(1, 2, 3, 4, 5, 6, 7, 8, 9, 0);


// 10. 객체에서 원하는 키-값을 추출
let obj11 = {
    x4: 1,
    y4: 2,
    z4: (p, q) => {
        console.log(this.x4 + this.y4 + p + q);
    }
};
let {x4, y4} = obj11;
let {z4} = obj11;
z4(3, 4); // 이렇게 사용하면 this가 불분명하기 때문에 사용x
z4.call(obj4, 3, 4); // 이렇게 사용하면 z4 내부의 this를 obj4로 결정하고 사용할 수 있어서 x4와 y4가 분명해진다


// 11. 아키텍쳐 모듈
// 이벤트 모듈
const EventEmitter = require('events');

const myEvent1 = new EventEmitter();
myEvent1.on('event1', () => {
    console.log('event1 발생');
});
myEvent1.on('event2', () => {
    console.log('event2 발생');
});

myEvent1.emit('event1');
myEvent1.emit('event2');

myEvent1.once('event3', () => {
    console.log('event3 발생');
});
myEvent1.emit('event3');
myEvent1.emit('event3');

// 이벤트 객체의 생성자를 상속받아서 다른 객체도 이벤트를 사용할 수 있어야 한다
const util = require('util');

const domObject = function () {
    this.on('message', function (e) {
        console.log('message 이벤트 발생');
        console.log(`받은 메세지: ${e.msg}`)
    })
};
util.inherits(domObject, EventEmitter); // domObject가 이벤트이미터 객체의 생성자를 상속받는다
let domObject1 = new domObject();
domObject1.emit('message', {msg: 'hello world'});


// 콘솔객체
console.log('hello world');
console.error('hello world');
let timeChecker;
console.time(timeChecker);
for (let i = 0; i <= 10; i++) {
}
console.timeEnd(timeChecker);
