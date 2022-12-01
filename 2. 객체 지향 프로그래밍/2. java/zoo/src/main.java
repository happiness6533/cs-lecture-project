import java.util.ArrayList;

public class main {
    public static void main(String[] args) {
        ArrayList<abstractAnimal> animals = new ArrayList<>();

        animals.add(new cat("맥스"));
        animals.add(new dog("심바"));
        animals.add(new pig("품바"));

        for (abstractAnimal animal : animals) {
            System.out.print(animal.name + "의 울음 소리: ");
            animal.cry();
        }
    }
}