
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        StringBuilder sb = new StringBuilder();
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        for (int i = 1; i <= 9; i++) {
            sb.append(N).append(" * ").append(i).append(" = ").append(N*i).append("\n");
        }
        System.out.println(sb);
    }
}
