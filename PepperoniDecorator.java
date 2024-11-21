public class PepperoniDecorator extends ToppingDecorator {
    public PepperoniDecorator(Pizza pizza) {
        super(pizza);
    }
    public String getDescription() {
        return pizza.getDescription().concat(" pepperoni");
    }
    public double getCost() {
        return pizza.getCost() + 1.5;
    }
}