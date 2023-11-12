class Solution {
    public int solution(int a, int b) {
        String sum1 = Integer.toString(a)+Integer.toString(b);
        String sum2 = Integer.toString(b)+Integer.toString(a);
        int answer1 = Integer.parseInt(sum1);
        int answer2 = Integer.parseInt(sum2);
        
        int answer = Math.max(answer1,answer2);
        return answer;
    }
}