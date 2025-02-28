
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int T = Integer.parseInt(br.readLine());
        for(int i = 0; i<T;i++){
            int n = Integer.parseInt(br.readLine());
            long[][] dp = new long[2][n+1];
            long[][] data = new long[2][n+1];

            //data 배열 초기화
            st = new StringTokenizer(br.readLine()," ");
            for(int j = 1; j<n+1;j++){
                data[0][j] = Integer.parseInt(st.nextToken());
            }
            st = new StringTokenizer(br.readLine()," ");
            for(int j = 1; j<n+1;j++){
                data[1][j] = Integer.parseInt(st.nextToken());
            }

            dp[0][1] = data[0][1];
            dp[1][1] = data[1][1];

            for(int j = 2; j<n+1;j++){
                dp[0][j] = Math.max(dp[1][j-1],dp[1][j-2]) + data[0][j];
                dp[1][j] = Math.max(dp[0][j-1],dp[0][j-2]) + data[1][j];
            }
            long result = Math.max(dp[0][n], dp[1][n]);
            System.out.println(result);
        }
    }
}
