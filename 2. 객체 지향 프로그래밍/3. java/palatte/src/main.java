import java.util.ArrayList;

public class main {
    public static void main(String[] args) {
        ArrayList<printable> shapes = new ArrayList<>();

        shapes.add(new rectangle(3, 4));
        shapes.add(new rectangle(4, 2));
        shapes.add(new square(3));
        shapes.add(new square(1));

        for (printable shape : shapes) {
            shape.print();
            System.out.println("---------");
        }
    }
}