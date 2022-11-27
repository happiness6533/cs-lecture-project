import java.util.ArrayList;

public class artist {
    //아티스트 기본속성 설정
    String name;
    private ArrayList<album> albumlist = new ArrayList<>();

    //아티스트 스킬생성
    //스킬1.아티스트 창조
    public artist(String name) {
        this.name = name;
    }

    //스킬2.앨범 추가
    public void addAlbum(album album) {
        albumlist.add(album);
    }

    //스킬3.앨범 고르기
    ArrayList<album> getAlbums() {
        return albumlist;
    }
}