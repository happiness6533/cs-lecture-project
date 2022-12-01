const L = require('./L.js');

// 프로미스 해결사
const promiseSolver = (a, f) => a instanceof Promise ? a.then(a => a) : f(a);

// 커리
const curry = f => (a, ..._) => _.length ? f(a, ..._) : (..._) => f(a, ..._);

// 맵
const map = curry(function* (f, iter) {
    for (const a of iter) {
        yield promiseSolver(a, f);
    }
});

// 필터
const filter = curry(function* (f, iter) {
    for (const a of iter) {
        const aSolved = promiseSolver(a, f);
        if (aSolved instanceof Promise) {
            yield aSolved.then(b => b ? a : Promise.reject())
        } else if (aSolved) {
            yield a
        }
    }
});

// 테이크
const take = L.curry((limit, iter) => {
    return L.take(limit, [...iter])
});

// 리듀스
const reduce = L.curry((f, acc, iter) => {
    iter
        ? L.reduce(f, acc, [...iter])
        : L.reduce(f, [...acc])
});


// 컴퓨터 자원을 최대로 써서, 빠르게 답을 도출할 때
const C = {
    curry,
    map,
    filter,
    take,
    reduce,
};

module.exports = C;