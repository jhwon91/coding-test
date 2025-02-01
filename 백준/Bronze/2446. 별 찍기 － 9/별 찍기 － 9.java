
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        for (int i = 1; i <= N; i++) {
            System.out.println(" ".repeat(i-1) + "*".repeat((N*2-1) - ((i-1) * 2)));
        }
        for (int i = N-1; i >= 1; i--) {
            System.out.println(" ".repeat(i-1) + "*".repeat((N*2-1) - ((i-1) * 2)));
        }
    }
}
