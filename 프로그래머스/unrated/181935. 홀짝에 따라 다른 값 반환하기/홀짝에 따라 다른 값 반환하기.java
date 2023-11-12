class Solution {
    public int solution(int n) {
        int answer = 0;
        if(n%2 ==1) {
            //홀수일 때 n보다 작은 홀수 다 더하기
            for (int i=0; 2*i+1<=n; i++) {
                answer += 2*i+1;   
            }
            
        } else {
            //짝수일 때 짝수제곱의 합
            for (int j = 0; 2*j<=n; j++) {
                 answer += Math.pow(2*j,2);
                
            }
        }
        return answer;
    }
}