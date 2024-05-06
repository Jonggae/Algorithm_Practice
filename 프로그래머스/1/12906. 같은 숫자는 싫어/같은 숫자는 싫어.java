import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        Stack<Integer> stack = new Stack<>();
        int length = arr.length;
          for (int i = 0; i <length; i++) {
           if (!stack.isEmpty() && stack.peek()==arr[i]) {
               stack.pop();
               stack.push(arr[i-1]);

           }else{
               stack.push(arr[i]);
           }

        }
int[] answer = new int[stack.size()];

        for (int i = 0; i <stack.size() ; i++) {
            answer[i] = stack.get(i);

        }
        return answer;
    }
}