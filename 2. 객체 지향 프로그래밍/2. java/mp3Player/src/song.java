public class song {
    //송 기본특성
    String title;
    //송 기본특성 - 다른 캐릭
    artist artist;
    album album;

    //송 스킬생성
    //스킬1.송 창조
    public song(String title, artist artist, album album) {
        this.title = title;
        this.artist = artist;
        this.album = album;
    }

    //스킬2.송 보여주기(이부분을 잘 모르겠습니다! public, String이 필수같은데 왜죠? 오버라이드 같은데 정확하게 모르겠어서ㅜ 질문드립니다!)
    public String toString() {
        return title + " - " + artist.name + "\n" + album.name + "(" + album.year + ")";
    }
}
