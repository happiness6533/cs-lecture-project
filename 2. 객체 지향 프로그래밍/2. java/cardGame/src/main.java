public class main {
    public static void main(String[] args) {
        blackjackHand hand1 = new blackjackHand();
        hand1.addCard(new blackjackCard(3, 1));
        hand1.addCard(new blackjackCard(4, 11));
        System.out.println(hand1.getValue());
        System.out.println(hand1.isBlackjack());
        System.out.println(hand1.isBusted());

        blackjackHand hand2 = new blackjackHand();
        hand2.addCard(new blackjackCard(1, 4));
        hand2.addCard(new blackjackCard(2, 8));
        hand2.addCard(new blackjackCard(2, 9));
        System.out.println(hand2.getValue());
        System.out.println(hand2.isBlackjack());
        System.out.println(hand2.isBusted());

        blackjackHand hand3 = new blackjackHand();
        hand3.addCard(new blackjackCard(2, 5));
        hand3.addCard(new blackjackCard(4, 9));
        hand3.addCard(new blackjackCard(2, 13));
        System.out.println(hand3.getValue());
        System.out.println(hand3.isBlackjack());
        System.out.println(hand3.isBusted());

        blackjackHand hand4 = new blackjackHand();
        hand4.addCard(new blackjackCard(2, 8));
        hand4.addCard(new blackjackCard(1, 1));
        System.out.println(hand4.getValue());
        System.out.println(hand4.isBlackjack());
        System.out.println(hand4.isBusted());

        blackjackHand hand5 = new blackjackHand();
        hand5.addCard(new blackjackCard(1, 7));
        hand5.addCard(new blackjackCard(1, 9));
        hand5.addCard(new blackjackCard(3, 1));
        System.out.println(hand5.getValue());
        System.out.println(hand5.isBlackjack());
        System.out.println(hand5.isBusted());

        blackjackHand hand6 = new blackjackHand();
        hand6.addCard(new blackjackCard(2, 1));
        hand6.addCard(new blackjackCard(1, 1));
        System.out.println(hand6.getValue());
        System.out.println(hand6.isBlackjack());
        System.out.println(hand6.isBusted());
    }
}