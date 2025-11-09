import java.util.Scanner;

public class QueueAtTheSchool {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int t = scanner.nextInt();

        scanner.nextLine();

        String s = scanner.nextLine();

        scanner.close();
        StringBuilder queue = new StringBuilder(s);

        for (int time = 0; time < t; time++) {
            for (int i = 0; i < n - 1; i++) {
                if (queue.charAt(i) == 'B' && queue.charAt(i + 1) == 'G') {
                    queue.setCharAt(i, 'G');
                    queue.setCharAt(i + 1, 'B');
                    i++;
                }
            }
        }
        System.out.println(queue);
    }
}