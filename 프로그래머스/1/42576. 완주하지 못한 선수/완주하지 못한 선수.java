import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        
        HashMap<String,Integer> map = new HashMap<>();
        
        for(String item:participant){
             map.put(item, map.getOrDefault(item, 0) + 1);
        }
        
        for(String item:completion){
            map.put(item, map.get(item)-1);
        }
        
        for (String i: map.keySet()){
            if(map.get(i) == 1){
                answer = i;
            }
        }
	
        
        return answer;
    }
}