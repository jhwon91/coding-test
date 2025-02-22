class Solution {
    public String solution(String my_string, int[][] queries) {
        char[] arrChar = my_string.toCharArray();
        
        for(int i = 0; i<queries.length;i++){
            int start = queries[i][0];
            int end = queries[i][1];
            
            while(start<end){
                char temp = arrChar[start];
                arrChar[start++] = arrChar[end];
                arrChar[end--] = temp;
            }
        }
        
        return new String(arrChar);
    }
}