class Solution {
    public int solution(int n) {
        int answer = 0;
        boolean mode;
        
        if (n % 2 == 0){
            mode = true;
        }else {
            mode = false;           
        }
        
        for(int i = 1; i<=n; i++){
            if (mode) {
                if (i % 2 ==0){answer += i*i;}
            }else{
                if (i % 2 ==1){answer += i;}
            }
        }
        
        return answer;
    }
}