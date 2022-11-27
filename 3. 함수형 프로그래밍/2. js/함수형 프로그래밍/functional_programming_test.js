const L = require('./L.js');
const C = require('./C.js');

// 객체 지향 프로그래밍은 연관있는 데이터와 함수를 객체로 관리한다
// 객체끼리의 상호작용을 통해 데이터를 변화시켜 나간다

// 함수형 프로그래밍은 데이터와 함수를 분리한다
// 불변성을 지키는 순수 함수를 만들고 조합해서 데이터를 변화시켜 나간다
//

const delaySquare = (x) => {
    return new Promise(resolve => {
        setTimeout(() => {
            return resolve(x * x)
        }, 1000)
    })
};

const add = (a, b) => {
    return a + b
};

console.time();
L.go([1, 2, 3, 4, 5, 6, 7, 8, 9],
    L.map(delaySquare),
    L.take(5),
    L.reduce(add),
    console.log,
    () => console.timeEnd()
);

console.time();
L.go([1, 2, 3, 4, 5, 6, 7, 8, 9],
    L.map(delaySquare),
    C.take(5),
    L.reduce(add),
    console.log,
    () => console.timeEnd()
);