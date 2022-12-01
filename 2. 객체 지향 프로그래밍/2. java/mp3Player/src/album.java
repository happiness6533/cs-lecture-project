import java.util.ArrayList;

public class album {
    //앨범 기본속성 설정
    artist artist;
    String name;
    int year;
    private ArrayList<song> songlist = new ArrayList<>();

    //앨범 스킬생성
    //스킬1.앨범 창조
    public album(String name, int year, artist artist) {
        this.name = name;
        this.year = year;
        this.artist = artist;
    }

    //스킬2.송 추가
    void addTrack(song song) {
        songlist.add(song);
    }

    //스킬3.송 고르기
    song getTrack(int i) {
        return songlist.get(i - 1);
    }
}
