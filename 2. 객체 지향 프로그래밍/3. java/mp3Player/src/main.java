public class main {

    public static void main(String[] args) {
        artist keithJarrett = new artist("Keith Jarrett");

        album theMelodyAtNightWithYou = new album("The Melody At Night With You", 1999, keithJarrett);
        theMelodyAtNightWithYou.addTrack(new song("I Loves You, Porgy", keithJarrett, theMelodyAtNightWithYou));
        theMelodyAtNightWithYou.addTrack(new song("I Got It Bad (and That Ain't Good)", keithJarrett, theMelodyAtNightWithYou));
        theMelodyAtNightWithYou.addTrack(new song("Don't Ever Leave Me", keithJarrett, theMelodyAtNightWithYou));
        theMelodyAtNightWithYou.addTrack(new song("Someone to Watch over Me", keithJarrett, theMelodyAtNightWithYou));

        album insideOut = new album("Inside Out", 2001, keithJarrett);
        insideOut.addTrack(new song("From the Body", keithJarrett, insideOut));
        insideOut.addTrack(new song("Inside Out", keithJarrett, insideOut));

        keithJarrett.addAlbum(theMelodyAtNightWithYou);
        keithJarrett.addAlbum(insideOut);

        artist bts = new artist("방탄소년단");

        album darkAndWild = new album("DARK & WILD", 2014, bts);
        darkAndWild.addTrack(new song("Intro: What am I to You", bts, darkAndWild));
        darkAndWild.addTrack(new song("Danger", bts, darkAndWild));

        album wings = new album("WINGS", 2016, bts);
        wings.addTrack(new song("Intro: Boy Meets Evil", bts, wings));
        wings.addTrack(new song("피 땀 눈물", bts, wings));
        wings.addTrack(new song("Begin", bts, wings));
        wings.addTrack(new song("Lie", bts, wings));


        bts.addAlbum(darkAndWild);
        bts.addAlbum(wings);

        System.out.println(keithJarrett.getAlbums().get(0).getTrack(2).toString());
        System.out.println();
        System.out.println(bts.getAlbums().get(1).getTrack(3).toString());
    }
}