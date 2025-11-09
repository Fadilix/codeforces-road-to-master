import java.util.Scanner;

public class CalculatingFunction {
    public static long calculate(long n) {
        long result = (long) Math.ceil(n / 2.0); 

        if (n % 2 == 0) {
            return result;
        } 

        return - result;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        long n = scanner.nextLong();
        System.out.println(CalculatingFunction.calculate(n));
        scanner.close();
    }
}