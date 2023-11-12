class Solution {
    public String solution(String[] arr) {
        StringBuilder sb = new StringBuilder();
        String answer = "";
       
        for (int i=0; i<arr.length; i++) {
            answer = String.valueOf(sb.append(arr[i]));
            
        }
        return answer;
    }
}