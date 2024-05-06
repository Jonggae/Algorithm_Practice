import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] solution(String s) {
        int[] answer = new int[s.length()];
        Map<Character, Integer> indexes = new HashMap<>();
        
        for (int i = 0; i < s.length(); i++) {
            char currentChar = s.charAt(i);

            if (indexes.containsKey(currentChar)) {
                int lastIndex = indexes.get(currentChar);
                answer[i] = i - lastIndex; 
            } else {
                answer[i] = -1;
            }
            indexes.put(currentChar, i);

        }
        
        return answer;
    }
}