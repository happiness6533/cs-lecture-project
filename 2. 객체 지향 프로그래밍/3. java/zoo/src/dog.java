public class dog extends abstractAnimal {
    public dog(String name) {
        super(name);
    }

    @Override
    public void cry() {
        System.out.println("왈왈");
    }
}

