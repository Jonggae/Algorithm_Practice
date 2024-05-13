class Solution {
    public long solution(int a, int b) {
        long answer = 0;

        if (a > b) {
            // a와 b를 교환하여 a가 항상 작도록 함
            int temp = a;
            a = b;
            b = temp;
        }

        // 합 계산
        answer = ((long)(a + b) * (b - a + 1)) / 2;

        return answer;
    }
}