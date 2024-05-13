import java.util.ArrayList;
import java.util.Arrays;
class Solution {
    public int[] solution(int[] arr, int divisor) {
        ArrayList<Integer> answerArray = new ArrayList<>();
         for (int i = 0; i <arr.length ; i++) {
            if(arr[i] %divisor ==0) {
                answerArray.add(arr[i]);
            }

        }
                int[] answer = {};

         if (answerArray.size()==0) {
            answer = new int[]{-1};
        }  else {
            answer = new int[answerArray.size()];
            for (int i = 0; i < answerArray.size() ; i++) {
                answer[i] = answerArray.get(i);

            }
        }
        Arrays.sort(answer);
        
        return answer;
    }
}