public class pokemon {
    public final String name;
    public final int cp;

    public pokemon(String name, int cp) {
        this.name = name;
        this.cp = cp;
    }

    @Override
    public String toString() {
        return name + "(" + cp + ")";
    }
}
