import java.util.ArrayList;
import java.util.HashMap;

public class pokemonBag {
    private final HashMap<String, ArrayList<pokemon>> pokemons = new HashMap<>();

    public void add(pokemon pokemon) {
        if (pokemons.get(pokemon.name) == null) {
            pokemons.put(pokemon.name, new ArrayList<>());
        }
        pokemons.get(pokemon.name).add(pokemon);
    }

    public ArrayList<pokemon> getPokemons(String name) {
        return pokemons.get(name);
    }

    public pokemon getStrongest(String name) {
        if (getPokemons(name) == null) {
            return null;
        } else {
            int keycp = getPokemons(name).get(0).cp;
            int keyindex = 0;

            for (int i = 0; i <= getPokemons(name).size() - 1; i++) {
                if (getPokemons(name).get(i).cp > keycp) {
                    keycp = getPokemons(name).get(i).cp;
                    keyindex = i;
                }
            }
            return getPokemons(name).get(keyindex);
        }
    }

    public pokemon getStrongest() {
        ArrayList<pokemon> powermons = new ArrayList<>();

        for (String name : pokemons.keySet()) {
            powermons.add(getStrongest(name));
        }

        int firstcp = powermons.get(0).cp;
        int keyindex = 0;

        for (int i = 0; i <= powermons.size() - 1; i++) {
            if (powermons.get(i).cp > firstcp) {
                firstcp = powermons.get(i).cp;
                keyindex = i;
            }
        }

        return powermons.get(keyindex);
    }
}