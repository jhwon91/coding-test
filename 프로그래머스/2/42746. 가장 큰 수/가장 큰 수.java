import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        String answer = "";
        String[] strNumbers = Arrays.stream(numbers)
                            .mapToObj(String::valueOf)
                            .toArray(String[]::new);
        
        // Arrays.stream(strNumbers).forEach(e -> System.out.println(e));
        Arrays.sort(strNumbers, (a,b) -> (b + a).compareTo(a+b));
        if(strNumbers[0].equals("0")) return "0";
        return String.join("",strNumbers);
    }
}