import java.util.Arrays;

class Solution {
    public String solution(String s) {
        StringBuilder sb = new StringBuilder();
        char[] c = s.toCharArray();
        int[] charToNum = new int[s.length()];
             for (int i = 0; i < s.length(); i++) {
            charToNum[i] = c[i];

        }
        Arrays.sort(charToNum);
        
          for (int i = s.length()-1; i >=0 ; i--) {
            sb.append((char) charToNum[i]);

        }
        
        String answer = String.valueOf(sb);
        return answer;
    }
}