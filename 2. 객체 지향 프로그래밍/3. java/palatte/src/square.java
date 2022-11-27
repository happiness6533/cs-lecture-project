public class square extends abstractShape implements printable {
    // 길이
    double side;

    // 생성자
    public square(double side) {
        super(0, 0);
        this.side = side;
    }

    // 넓이
    public double getArea() {
        return side * side;
    }

    // 둘레
    public double getPerimeter() {
        return 4 * side;
    }

    @Override
    public void print() {
        for (int i = 1; i <= side; i++) {
            for (int j = 1; j <= side; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
