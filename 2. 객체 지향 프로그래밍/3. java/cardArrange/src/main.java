import java.util.ArrayList;
import java.util.Collections;

public class main {
    public static void main(String[] args) {
        ArrayList<card> cards = new ArrayList<>();

        cards.add(new card(2, 6));
        cards.add(new card(4, 1));
        cards.add(new card(3, 11));
        cards.add(new card(3, 13));
        cards.add(new card(1, 7));
        cards.add(new card(3, 1));
        cards.add(new card(4, 12));
        cards.add(new card(1, 1));

        Collections.sort(cards);
        System.out.println(cards);
    }
}