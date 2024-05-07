import java.util.PriorityQueue;
class Solution {
    public int[] solution(int k, int[] score) {
        
        PriorityQueue<Integer> honor = new PriorityQueue<>(k);
        int[] answer = new int[score.length];
         for (int i = 0; i < score.length; i++) {
            if (honor.size() < k) {
                honor.add(score[i]); // 최대 k개까지 요소 유지
            } else if (honor.peek() < score[i]) {
                honor.poll(); // 최소 값 제거
                honor.add(score[i]);
            }

            // 현재 힙의 최소값을 결과에 저장
            answer[i] = honor.peek();
        }
        return answer;
    }
}