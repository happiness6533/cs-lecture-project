public class blackjackHand extends deck<blackjackCard> {

    // 메소드
    public int getValue() {
        int value = 0;

        for (blackjackCard card : getCards()) {
            value += card.getValue();
        }

        for (blackjackCard card : getCards()) {
            if (card.isAce() == true) {
                if (value > 21) {
                    value -= 10;
                }
            }
        }

        return value;
    }

    public boolean isBusted() {
        if (getValue() > 21) {
            return true;
        } else {
            return false;
        }
    }

    public boolean isBlackjack() {
        if (getCards().size() == 2 && getValue() == 21) {
            return true;
        } else {
            return  false;
        }
    }
}