import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int num = Integer.parseInt(br.readLine());
        long[][] dp = new long[num+1][10];
        dp[1][0] = 0;

        for(int i = 1; i< dp[1].length;i++){
            dp[1][i] = 1;
        }

        for(int i = 2; i< dp.length;i++){
            for(int j = 0; j<dp[i].length;j++){
                if (j == 0){
                    dp[i][j] = dp[i-1][j+1] % 1000000000;
                }else if (j == 9){
                    dp[i][j] = dp[i-1][j-1] % 1000000000;
                } else{
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1] % 1000000000;
                }
            }
        }

        System.out.print(Arrays.stream(dp[num]).sum() % 1000000000);
    }
}