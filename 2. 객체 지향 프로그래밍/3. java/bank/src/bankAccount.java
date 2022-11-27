public class bankAccount {
    private int balance;
    private person owner;


    // 입금함수
    boolean deposit(int amount) {
        if (amount >= 0 && amount <= owner.getCashAmount()) {
            balance += amount;
            owner.setCashAmount(owner.getCashAmount() - amount);
            System.out.println(amount + "원 입금하였습니다. 잔고: " + balance + "원, 현금: " + owner.getCashAmount() + "원");
            return true;
        } else {
            System.out.println("입금 실패입니다. 잔고: " + balance + "원, 현금: " + owner.getCashAmount() + "원");
            return false;
        }
    }


    // 출금함수
    boolean withdraw(int amount) {
        if (amount >= 0 && amount <= balance) {
            balance -= amount;
            owner.setCashAmount(owner.getCashAmount() + amount);
            System.out.println(amount + "원 출금하였습니다. 잔고: " + balance + "원, 현금: " + owner.getCashAmount() + "원");
            return true;
        } else {
            System.out.println("출금 실패입니다. 잔고: " + balance + "원, 현금: " + owner.getCashAmount() + "원");
            return false;
        }
    }


    // 잔액 세터 게터
    public void setBalance(int newbalance) {
        balance = newbalance;
    }
    public int getBalance() {
        return balance;
    }


    // 주인 세터 게터
    public void setOwner(person newowner) {
        owner = newowner;
    }
    public person getOwner() {
        return owner;
    }


    // 이체함수
    public boolean transfer(person to, int amount) {
        if (amount < 0 || amount > balance) {
            System.out.println("false - from: " + owner.getName() + ", to: " + to.getName() + ", amount: " + amount + ", balance: " + balance);
            return false;
        } else {
            balance -= amount;
            to.getAccount().setBalance(to.getAccount().getBalance() + amount);
            System.out.println("true - from: " + owner.getName() + ", to: " + to.getName() + ", amount: " + amount + ", balance: " + balance);
            return true;
        }
    }


    // 이체함수2
    public boolean transfer(bankAccount to, int amount) {
        if (amount < 0 || amount > balance) {
            System.out.println("false - from: " + owner.getName() + ", to: " + to.getOwner() + ", amount: " + amount + ", balance: " + balance);
            return false;
        } else {
            balance -= amount;
            to.setBalance(to.getBalance() + amount);
            System.out.println("true - from: " + owner.getName() + ", to: " + to.getOwner().getName() + ", amount: " + amount + ", balance: " + balance);
            return true;
        }
    }


    // 생성자
    public bankAccount(int pBalance) {
        if (pBalance < 0) {
            balance = 0;
        } else {
            balance = pBalance;
        }
    }


    // 생성자2
    public bankAccount(person pOwner) {
        owner = pOwner;
    }


    // 생성자3
    public bankAccount(int pBalance, person pOwner) {
        if (pBalance < 0) {
            balance = 0;
        } else {
            balance = pBalance;
        }

        owner = pOwner;
    }
}
