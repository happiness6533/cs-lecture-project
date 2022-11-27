public class main {
    public static void main(String[] args) {
        // 사람 선언
        person p1 = new person("김신의", 28);
        p1.setCashAmount(30000);

        bankAccount a1 = new bankAccount(p1);
        a1.setBalance(100000);

        // 남은 세팅
        p1.setAccount(a1);

        person p2 = new person("문종모", 25, 100000);
        bankAccount a2 = new bankAccount(500000, p2);
        p2.setAccount(a2);

        a2.transfer(a1, 200000);
        a1.transfer(p2, 150000);
        p2.transfer(a1, 270000);
        p1.transfer(p2, 130000);
    }
}