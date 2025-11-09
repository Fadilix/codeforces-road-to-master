import java.util.Collections;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Stream;

public class Presents {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();

        scanner.nextLine();

        List<Integer> p = Stream.of(scanner.nextLine().split(" ")).map(c -> Integer.valueOf(c)).toList();
        int min = Collections.min(p);

        if (min - 1 < 1) {
            System.out.println(p);
            System.exit(0);
        } 

        System.out.println(p.stream().map(pe -> pe -1).toList());

        scanner.close();

    }
}


// will finish later