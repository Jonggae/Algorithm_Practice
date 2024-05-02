class Solution {
    public int solution(int left, int right) {
        int answer = 0;
          for (int i = left; i <= right; i++) {
            // i의 제곱근이 정수인지 확인
            if (Math.sqrt(i) == (int) Math.sqrt(i)) {
                answer -= i; // 홀수 개수인 경우 (완전제곱수)
            } else {
                answer += i; // 짝수 개수인 경우
            }
        }
            
        return answer;
    }
}