// 커리
const curry = f => (a, ..._) => _.length ? f(a, ..._) : (..._) => f(a, ..._);

// 맵
const map = curry((f, iterable) => {
    let result = [];
    for (const el of iterable) {
        result.push(f(el));
    }
    return result;
});

// 필터
const filter = curry((f, iterable) => {
    let result = [];
    for (const el of iterable) {
        if (f(el)) {
            result.push(el)
        }
    }
    return result
});

// 리듀스
const reduce = curry((f, acc, iter) => {
    if (!iter) {
        iter = acc[Symbol.iterator]();
        acc = iter.next().value
    } else {
        iter = iter[Symbol.iterator]()
    }
    for (const el of iter) {
        acc = f(acc, el);
    }
    return acc
});

// 테이크
const take = curry((limit, iterable) => {
    let result = [];
    for (const el of iterable) {
        result.push(el);
        if (result.length === limit) {
            return result;
        }
    }
});

// 고 앤 파이프
const go = (...args) => reduce((a, f) => f(a), args);
const pipe = (f, ...fs) => (...as) => go(f(...as), ...fs);

const B = {
    curry,
    map,
    filter,
    take,
    reduce,
    go,
    pipe
};

module.exports = B;