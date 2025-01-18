import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        HashMap<String,Integer> map = new HashMap<>();
        for(String[] items: clothes){
            map.put(items[1], map.getOrDefault(items[1],0)+1);
        }
        
        
        for (int count : map.values()) {
            answer *= (count + 1); // 선택하지 않는 경우 포함
        }
        
        return answer-1;
    }
}