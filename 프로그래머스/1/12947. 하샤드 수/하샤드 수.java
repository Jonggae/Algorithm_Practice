class Solution {
    public boolean solution(int x) {
        boolean answer = true;
        int num = x;
         int sum = 0;

        while (num >= 10) {
            sum += num % 10;
            num = num / 10;

        }
        sum+= num;
          if (x % sum ==0) {
            answer = true;
        }else {
            answer = false;
        }
        
        return answer;
    }
}