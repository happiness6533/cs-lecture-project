public class card implements Comparable<card>{
    public final int suitNumber;
    public final int rankNumber;

    public card(int suitNumber, int rankNumber) {
        this.suitNumber = suitNumber;
        this.rankNumber = rankNumber;
    }

    public String getSuit() {
        switch (suitNumber) {
            case 1:
                return "Clubs";
            case 2:
                return "Diamonds";
            case 3:
                return "Hearts";
            case 4:
                return "Spades";
            default:
                return "";
        }
    }

    public String getRank() {
        switch (rankNumber) {
            case 1:
                return "Ace";
            case 11:
                return "Jack";
            case 12:
                return "Queen";
            case 13:
                return "King";
            default:
                return String.valueOf(rankNumber);
        }
    }

    public String toString() {
        return getRank() + " of " + getSuit();
    }

    @Override
    public int compareTo(card o) {
        if (suitNumber != o.suitNumber) {
            return suitNumber - o.suitNumber;
        } else {
            return rankNumber - o.rankNumber;
        }
    }
}
