
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int count = 0;
        for (int i = 0; i < N; i++) {
            String word = br.readLine();
            if(check(word)){
                count++;
            }
        }
        System.out.println(count);
    }

    public static boolean check(String word) {
        boolean[] checkArray = new boolean[26];
        int prev = -1;

        for (int i = 0; i < word.length(); i++) {
            int current = word.charAt(i) - 'a';

            if(current != prev){
                if(checkArray[current]){
                    return false;
                } else {
                    checkArray[current] = true;
                    prev = current;
                }
            }
        }
        return true;
    }
}
