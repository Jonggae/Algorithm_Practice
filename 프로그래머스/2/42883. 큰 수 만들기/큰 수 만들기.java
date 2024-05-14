import java.util.Stack;
class Solution {
    public String solution(String number, int k) {
        String answer = "";
        
         Stack<Character> stack = new Stack<>();

        char[] nums = number.toCharArray();

        for (int i = 0; i <number.length() ; i++) {
            while (k>0&&!stack.isEmpty()&&stack.peek()<nums[i]){
                stack.pop();
                k--; 

            }
            stack.push(nums[i]);
        }
         while (k > 0) {
        stack.pop();
        k--;
    }
        StringBuilder sb = new StringBuilder();
        while (!stack.isEmpty()) {
            sb.append(stack.pop());
        }
        sb.reverse();
        answer = String.valueOf(sb);
        return answer;
    }
}