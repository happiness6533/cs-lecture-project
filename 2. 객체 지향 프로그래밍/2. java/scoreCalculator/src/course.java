public class course {
    //캐릭터 Course의 기본속성설정
    String coursename;
    int credit;
    double score;
    //모든 Course 캐릭터의 공유속성설정
    static int CREDIT_MAJOR = 3;
    static int CREDIT_GENERAL = 2;

    //캐릭터 Course의 스킬생성
    //스킬1.Course 탄생
    public course(String coursename, int choose, String alphabetscore) {
        this.coursename = coursename;

        credit = choose;

        switch (alphabetscore) {
            case "A+":
                score = 4.5;
                break;
            case "A":
                score = 4;
                break;
            case "B+":
                score = 3.5;
                break;
            case "B":
                score = 3;
                break;
            case "C+":
                score = 2.5;
                break;
            case "C":
                score = 2;
                break;
            case "D+":
                score = 1.5;
                break;
            case "D":
                score = 1;
                break;
            case "F":
                score = 0;
                break;
            default:
                break;
        }
    }
}
