import java.util.*;
class Solution {
    public int[] solution(int N, int[] stages) {
         int[] countReached = new int[N+1];  // 각 스테이지에 도달한 플레이어 수
        int[] countStuck = new int[N+1];    // 각 스테이지에 멈춰 있는 플레이어 수

        // 스테이지에 도달한 플레이어 수 계산
        for(int stage : stages) {
            if(stage <= N) {
                countStuck[stage-1]++;
            }
            for(int i = 0; i < Math.min(stage, N); i++) {
                countReached[i]++;
            }
        }

        // 각 스테이지별 실패율 계산 및 엔트리 리스트에 추가
        List<Map.Entry<Integer, Double>> entries = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            double failureRate = countReached[i] == 0 ? 0 : (double) countStuck[i] / countReached[i];
            entries.add(new AbstractMap.SimpleEntry<>(i + 1, failureRate));
        }

        // 실패율을 기준으로 내림차순 정렬
        entries.sort((a, b) -> b.getValue().compareTo(a.getValue()));

        // 결과 배열 생성 및 결과값 할당
        int[] sortedIndex = new int[N];
        for (int i = 0; i < entries.size(); i++) {
            sortedIndex[i] = entries.get(i).getKey();
        }

        return sortedIndex;
    }
}