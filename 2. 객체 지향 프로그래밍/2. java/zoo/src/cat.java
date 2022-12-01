public class cat extends abstractAnimal {
    public cat(String name) {
        super(name);
    }

    @Override
    public void cry() {
        System.out.println("야옹");
    }
}
