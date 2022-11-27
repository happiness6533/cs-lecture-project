public class rectangle extends abstractShape implements printable {
    // 길이
    double side1; // 세로
    double side2; // 가로

    // 생성자
    public rectangle(double side1, double side2) {
        super(0, 0);
        this.side1 = side1;
        this.side2 = side2;
    }

    // 넓이
    public double getArea() {
        return side1 * side2;
    }

    // 둘레
    public double getPerimeter() {
        return 2 * (side1 + side2);
    }

    @Override
    public void print() {
        for(int i = 1; i <= side1; i++) {
            for( int j = 1; j <= side2; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
