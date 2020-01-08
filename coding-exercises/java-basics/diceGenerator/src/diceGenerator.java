import java.util.Random;

public class diceGenerator {
    public static void  main(String[] arguments)
    {
        Random generator = new Random();
        int value = generator.nextInt();
        System.out.println("The random number is"
        + value);
    }

}
