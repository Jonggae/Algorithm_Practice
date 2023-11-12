class Solution {
    public String solution(String str1, String str2) {
        StringBuilder sb = new StringBuilder();
        String answer = "";
        for (int i=0; i<str1.length(); i++) {
            answer = String.valueOf(sb.append(str1.charAt(i)));
            answer = String.valueOf(sb.append(str2.charAt(i)));
            
        }
        
        
        return answer;
    }
}