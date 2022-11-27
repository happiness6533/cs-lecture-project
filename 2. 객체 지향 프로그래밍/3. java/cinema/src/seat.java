public class seat {
    private String name;
    public String getName() {
        return this.name;
    }
    public void reserve(String name) {
        this.name = name;
    }
    public void cancel() {
        this.name = null;
    }
    public boolean isOccupied(){
        if (this.name != null) {
            return true;
        } else {
            return false;
        }
    }
    public boolean match(String checkName) {
        if (this.name == checkName) {
            return true;
        } else {
            return false;
        }
    }
}