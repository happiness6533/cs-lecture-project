public class gradeCalculator {
    //캐릭터 GradeCalculator의 기본속성
    String name;
    double Xexpectation;
    int Xsumcredit;

    double thisexpectation;
    int thissumcredit;

    double expectation;
    int sumcredit;

    //캐릭터 GradeCalculator 스킬생성
    //스킬1.GradeCalculator 탄생
    public gradeCalculator(String name, double Xexpectation, int Xsumcredit) {
        this.name = name;
        this.Xexpectation = Xexpectation;
        this.Xsumcredit = Xsumcredit;
    }

    //스킬2.캐릭터 Course의 참여 >> 캐릭터 GradeCalculator의 기본속성변경
    void addCourse(course course) {
        thisexpectation = (thissumcredit * thisexpectation + course.credit * course.score) / (thissumcredit + course.credit);
        thissumcredit = thissumcredit + course.credit;

        expectation = (Xexpectation * Xsumcredit + thisexpectation * thissumcredit) / (Xsumcredit + thissumcredit);
        sumcredit = Xsumcredit + thissumcredit;
    }

    //스킬3.캐릭터 GradeCalcilator의 기본속성정보 보여주기
    void print() {
        System.out.println("직전 학기 성적: " + Xexpectation + " (총 " + Xsumcredit + "학점)\n" +
                "이번 학기 성적: " + thisexpectation + " (총 " + thissumcredit + "학점)\n" +
                "전체 예상 학점: " + expectation + " (총 " + sumcredit + "학점)");
    }

    //아직 감을 못잡은 부분 : 퍼블릭, 프라이빗을 어떤 경우에 고려하는지 직감적으로 아직 모르겠습니다! 나머지는 괜찮네요...제 생각엔?ㅋㅋ
}