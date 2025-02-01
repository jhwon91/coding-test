
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        for(int i = 0 ; i<str.length();i += 10){
            System.out.println(str.substring(i,Math.min(i+10,str.length())));
        }
    }
}
