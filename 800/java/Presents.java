import java.util.ArrayList;
// import java.util.HashMap;
import java.util.List;
// import java.util.Map;
import java.util.Scanner;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Presents {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();

        scanner.nextLine();
        // Map<Integer, Integer> hashMap = new HashMap<>();


        List<Integer> friends = Stream.of(scanner.nextLine().split(" ")).map(e -> Integer.valueOf(e)).toList();
        List<Integer> result = new ArrayList<>();

        for (int i = 1; i < friends.size() + 1; i++) {
            result.add(friends.indexOf(i) + 1);
            // hashMap.put(friends.get(i), i);
        }


        String joined = result.stream().map(String::valueOf).collect(Collectors.joining(" "));
        System.out.println(joined);

        scanner.close();
    }
}