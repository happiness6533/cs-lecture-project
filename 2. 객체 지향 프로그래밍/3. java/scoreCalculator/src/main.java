public class main {
    public static void main(String[] args) {
        gradeCalculator gradeCalc = new gradeCalculator("김신의", 4.0, 100);

        gradeCalc.addCourse(new course("OOP", course.CREDIT_MAJOR, "A+"));
        gradeCalc.addCourse(new course("신호와시스템", course.CREDIT_MAJOR, "A"));
        gradeCalc.addCourse(new course("해석학", course.CREDIT_MAJOR, "B+"));
        gradeCalc.addCourse(new course("확률", course.CREDIT_MAJOR, "A+"));
        gradeCalc.addCourse(new course("스포츠댄스", course.CREDIT_GENERAL, "A"));

        gradeCalc.print();
    }
}