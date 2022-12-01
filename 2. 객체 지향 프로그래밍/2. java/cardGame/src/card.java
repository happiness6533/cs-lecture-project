public class card {
    // 모양과 숫자
    public final int suitNumber;
    public final int rankNumber;

    // 생성자
    public card(int suitNumber, int rankNumber) {
        this.suitNumber = suitNumber;
        this.rankNumber = rankNumber;
    }

    // 메소드
    public String getSuit() {
        String suit = new String();

        switch (suitNumber) {
            case 1:
                suit = "Clubs";
                break;
            case 2:
                suit = "Hearts";
                break;
            case 3:
                suit = "Diamonds";
                break;
            case 4:
                suit = "Spades";
                break;
        }

        return suit;
    }

    public String getRank() {
        String rank = new String();

        switch (rankNumber) {
            case 1:
                rank = "Ace";
                break;
            case 11:
                rank = "Jack";
                break;
            case 12:
                rank = "Queen";
                break;
            case 13:
                rank = "King";
                break;
            default:
                rank = String.valueOf(rankNumber);
                break;
        }

        return rank;
    }

    @Override
    public String toString() {
        return getRank() + " of " + getSuit();
    }
}