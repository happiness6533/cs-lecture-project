import java.util.ArrayList;
import java.util.Random;

public class deck<T> {
    // 변수 카드 리스트
    private ArrayList<T> cards = new ArrayList<>();

    // 메소드
    public void addCard(T card) {
        cards.add(card);
    }

    public ArrayList<T> getCards() {
        return cards;
    }

    public void print() {
        for (int i = 0; i <= cards.size() - 1; i++) {
            System.out.println(cards.get(i).toString());
        }
    }

    public void shuffle() {
        Random random = new Random();
        ArrayList<T> temp = new ArrayList<>();

        while (cards.size() >= 1) {
            int randomindex = random.nextInt(cards.size());
            temp.add(cards.get(randomindex));
            cards.remove(randomindex);
        }

        cards = temp;
    }

    public deck deal(int count) {
        // 핸드 생성
        deck<T> hand = new deck<>();

        // 추가와 제거
        if (count == 5) {
            while (count >= 1) {
                hand.addCard(cards.get(cards.size() - 1));
                cards.remove(cards.size() - 1);
                count--;
            }
        }

        // 리턴
        return hand;
    }
}