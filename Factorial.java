public class Factorial {
    public static void main(String[] args) {
        if (args.length == 0) {
            System.out.println("Please provide a number as command line argument.");
            return;
        }
        int num = Integer.parseInt(args[0]);
        long fact = 1;
        for (int i = 1; i <= num; i++) {
            fact *= i;
        }
        System.out.println("Factorial of " + num + " is " + fact);
    }
}