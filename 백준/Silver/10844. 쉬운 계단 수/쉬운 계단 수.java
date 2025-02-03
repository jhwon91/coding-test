
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        long MOD = 1000000000L;
        long[][] dp = new long[N + 1][10];
        dp[1][0] = 0;
        for (int i = 1; i < dp[1].length; i++) {
            dp[1][i] = 1;
        }

        for (int i = 2; i <=N; i++) {
            for (int j = 0; j < dp[i].length; j++) {
                if (j == 0) {
                    dp[i][j] = dp[i-1][1] % MOD;
                }else if (j == 9){
                    dp[i][j] = dp[i-1][8] % MOD;
                }else {
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1] % MOD;
                }
            }
        }

        long result = Arrays.stream(dp[N]).sum() % MOD;
        System.out.println(result);

    }
}
