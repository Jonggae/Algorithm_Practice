class Solution {
    public int solution(int a, int b) {
        StringBuilder sb1 = new StringBuilder();
        StringBuilder sb2 = new StringBuilder();
        
        sb1.append(a).append(b);
        
        int answer1 = Integer.parseInt(sb1.toString());
        int answer3 = 2*a*b;
        
        
        int answer = Math.max(answer3,answer1);
        
            
        
        return answer;
    }
}