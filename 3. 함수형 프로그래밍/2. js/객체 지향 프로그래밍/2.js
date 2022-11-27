// 추상화 캡슐화 상속 다형성
class BankAccount {
    // 스태틱
    static pi = 3.14;
    static sayHi = () => {
        console.log("hi")
    }


    constructor(name, money) {
        this.holder = name;
        this.balance = money;
    }

    // getter
    get holder() {
        return this._holder;
    }

    // setter method
    set holder(holderName) {
        // 캡슐화
        this._holder = holderName;
    }

    deposit(money) {
        this.balance += money;
    }

    withdraw(money) {
        if (this.balance - money < 0) {
            console.log('Insufficient balance');
        } else {
            this.balance -= money;
        }
    }

    transfer(money, anotherAccount) {
        const account = anotherAccount;
        if (this.balance - money < 0) {
            console.log('Insufficient balance');
        } else {
            this.balance -= money;
            account.balance += money;
        }
    }
}

class PremiumBankAccount extends BankAccount {
    constructor(name, money, premiumCode) {
        super(name, money);
        this.premiumCode = premiumCode;
    }

    // 오버라이딩, 다형성
    deposit(money) {
        super.deposit(money);
        this.balance += 10000;
    }
}

// 객체 instanceof 클래스: 참 거짓을 리턴해 준다

// 사실 자바스크립트에는 캡슐화를 자체적으로 지원하는 문법이 아직 없습니다
// _holder로 접근하면 얼마든지 접근이 가능하기 때문이죠!
// Java는 private이라는 키워드가 있어서 언어의 문법 차원에서 캡슐화를 지원

// 하지만 JavaScript에서도 다른 방식으로 우회해서 완벽한 캡슐화를 할 수는 있는데
// 클로저(Closure)라고 하는 개념을 응용해서 적용하면 됨
function createUser(email, birthdate) {
    let _email = email;

    const user = {
        birthdate,

        get email() {
            return _email;
        },

        set email(address) {
            if (address.includes('@')) {
                _email = address;
            } else {
                throw new Error('invalid email address');
            }
        },
    };

    return user;
}

const user1 = createUser('chris123@google.com', '19920321');