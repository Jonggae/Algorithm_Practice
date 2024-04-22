import java.util.Stack;
class Solution {
    public int solution(String s) {
        
        String[] element = s.split(" ");
        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < element.length ; i++) {
            if(element[i].equals("Z")) {
                stack.pop();
            } else {
                stack.push(Integer.parseInt(element[i]));
            }

        }
        int sum=0;
        for (int i = 0; i < stack.size() ; i++) {

            sum += stack.elementAt(i);

        }
        return sum;
    }
}