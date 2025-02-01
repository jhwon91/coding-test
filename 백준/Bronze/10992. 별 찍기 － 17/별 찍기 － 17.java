
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        for (int i = 1; i <= N; i++) {
            System.out.print(" ".repeat(N-i));
            if(i == 1 || i == N) {
                System.out.println("*".repeat(2*i-1));
            } else {
                System.out.print("*");
                System.out.print(" ".repeat(2*(i-1) - 1));
                System.out.println("*");
            }
        }
    }
}
