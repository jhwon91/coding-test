
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        long MOD = 10007;
        long[][] dp = new long[N + 1][10];

        for (int i = 0; i < dp[1].length; i++) {
            dp[1][i] = 1;
        }

        for (int i = 2; i <= N ; i++) {
            for (int j = 0; j < dp[i].length; j++) {
                dp[i][j] = 0;

                for (int k = 0; k <= j; k++) {
                    dp[i][j] = (dp[i][j] + dp[i-1][k]) % MOD;
                }
            }
        }

        long result = Arrays.stream(dp[N]).sum() % MOD;
        System.out.println(result);

    }
}
