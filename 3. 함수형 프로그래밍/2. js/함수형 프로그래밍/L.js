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

// 리듀스
const reduce = curry((f, acc, iter) => {
    if (!iter) {
        iter = acc[Symbol.iterator]();
        acc = iter.next().value
    } else {
        iter = iter[Symbol.iterator]()
    }
    return promiseSolver(acc, function recursive(acc) {
        let cur = iter.next();
        while (!cur.done) {
            const a = cur.value;
            acc = f(acc, a);
            if (acc instanceof Promise) {
                return acc.then(res => recursive(res))
            }
            cur = iter.next();
        }
        return acc;
    });
});

// 테이크
const take = curry((limit, iter) => {
    let result = [];
    iter = iter[Symbol.iterator]();
    return (function recur() {
        let cur;
        while (!(cur = iter.next()).done) {
            const a = cur.value;
            if (a instanceof Promise) {
                return a
                    .then(a => {
                        result.push(a);
                        if (result.length === limit) {
                            return result
                        }
                        return recur()
                    })
                    .catch(e => Promise.reject(e));
            }
            result.push(a);
            if (result.length === limit) {
                return result
            }
        }
        return result;
    })();
});

// 고 앤 파이프
const go = (...args) => reduce((a, f) => f(a), args);
const pipe = (f, ...fs) => (...as) => go(f(...as), ...fs);

// 컴퓨터 자원을 최소화 해서, 하고자 하는 일만 처리할 때
const L = {
    curry,
    map,
    filter,
    take,
    reduce,
    go,
    pipe
};

module.exports = L;