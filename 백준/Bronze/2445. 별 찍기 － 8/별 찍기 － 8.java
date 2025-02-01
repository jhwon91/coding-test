
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt() * 2;

        for (int i = 1; i < N; i++) {
            if (N - (i*2) >= 0){
                for (int j = 0; j < i; j++) {
                    System.out.print("*");
                }

                for (int j = 0; j < N - (i*2); j++) {
                    System.out.print(" ");
                }

                for (int j = 0; j < i; j++) {
                    System.out.print("*");
                }
            }else {
                for (int j = 0; j < N-i; j++) {
                    System.out.print("*");
                }

                for (int j = 0; j < Math.abs(N - (i*2)); j++) {
                    System.out.print(" ");
                }

                for (int j = 0; j < N-i; j++) {
                    System.out.print("*");
                }
            }

            System.out.println();
        }
    }
}

