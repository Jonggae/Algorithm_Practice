import java.util.Arrays;
class Solution {
    public int solution(String s) {
        String[] element = s.split(" ");
        for (int i = 0; i <element.length ; i++) {
            if(element[i].equals("Z")) {
                element[i - 1] = "0";
                element[i] = "0";
            }
      }
        int[] num = new int[element.length];
        int answer = 0;
        for (int i = 0; i < element.length ; i++) {
            num[i] = Integer.parseInt(element[i]);
            answer+=num[i];
        }
        return answer;
    }
}