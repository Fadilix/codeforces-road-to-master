import java.util.Scanner;

public class GeorgeAndAccomodation {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        scanner.nextLine();

        int count = 0;
        for (int i = 0; i < n; i++) {
            int p = scanner.nextInt();
            int q = scanner.nextInt();
            if ((q - p) >= 2)
                count++;
        }
        scanner.close();

        System.out.println(count);
    }
}