import java.util.Scanner;

public class Magnets {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        scanner.nextLine();

        String prev = scanner.nextLine();

        int groups = 1;

        for (int i = 1; i < n; i++) {
            String current = scanner.nextLine();

            if (!current.equals(prev))
                groups++;
            prev = current;
        }

        System.out.println(groups);
        scanner.close();
    }
}