public class person {
    private String name;
    private int age;
    private int cashAmount;
    private bankAccount account;


    // 이름 세터 게터
    public void setName(String newname) {
        name = newname;
    }
    public String getName() {
        return name;
    }


    // 나이 세터 게터
    public void setAge(int newage) {
        age = newage;
    }
    public int getAge() {
        return age;
    }


    // 현금 세터 게터
    public void setCashAmount(int newcashAmount) {
        cashAmount = newcashAmount;
    }
    public int getCashAmount() {
        return cashAmount;
    }


    // 계좌 세터 게터
    public void setAccount(bankAccount newaccount) {
        account = newaccount;
    }
    public bankAccount getAccount() {
        return account;
    }


    // 이체함수
    public boolean transfer(person to, int amount) {
        if (amount < 0 || amount > account.getBalance()) {
            System.out.println("false - from: " + name + ", to: " + to.getName() + ", amount: " + amount + ", balance: " + account.getBalance());
            return false;
        } else {
            account.setBalance(account.getBalance() - amount);
            to.getAccount().setBalance(to.getAccount().getBalance() + amount);
            System.out.println("true - from: " + name + ", to: " + to.getName() + ", amount: " + amount + ", balance: " + account.getBalance());
            return true;
        }
    }


    // 이체함수2
    public boolean transfer(bankAccount to, int amount) {
        if (amount < 0 || amount > account.getBalance()) {
            System.out.println("false - from: " + name + ", to: " + to.getOwner().getName() + ", amount: " + amount + ", balance: " + account.getBalance());
            return false;
        } else {
            account.setBalance(account.getBalance() - amount);
            to.setBalance(to.getBalance() + amount);
            System.out.println("true - from: " + name + ", to: " + to.getOwner().getName() + ", amount: " + amount + ", balance: " + account.getBalance());
            return true;
        }
    }


    // 생성자
    public person(String pName, int pAge) {
        name = pName;

        if (pAge < 0) {
            age = 12;
        } else {
            age = pAge;
        }

        cashAmount = 0;
    }


    // 생성자2
    public person(String pNname, int pAge, int pCashAmount) {
        name = pNname;

        if (pAge < 0) {
            age = 12;
        } else {
            age = pAge;
        }

        if (pCashAmount < 0) {
            cashAmount = 0;
        } else {
            cashAmount = pCashAmount;
        }
    }
}
