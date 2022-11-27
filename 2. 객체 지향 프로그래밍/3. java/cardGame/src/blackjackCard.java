public class blackjackCard extends card {
    // 변수
    private int value;

    // 생성자
    public blackjackCard(int suitNumber, int rankNumber) {
        super(suitNumber, rankNumber);
    }

    // 메소드
    public int getValue() {
        switch (getRank()) {
            case "Ace":
                value = 11;
                break;
            case "Jack":
                value = 10;
                break;
            case "Queen":
                value = 10;
                break;
            case "King":
                value = 10;
                break;
            default:
                value = Integer.valueOf(getRank());
        }

        return value;
    }

    public boolean isAce() {
        if (getRank() == "Ace") {
            return true;
        } else {
            return  false;
        }
    }
}