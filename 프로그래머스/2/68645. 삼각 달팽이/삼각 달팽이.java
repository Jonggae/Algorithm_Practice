import java.util.Arrays;
class Solution {
    public int[] solution(int n) {
       int[] answer = new int[n*(n+1)/2];
        int[][] triangle = new int[n][];
        for (int i = 0; i <n ; i++) {
            triangle[i] = new int[i+1];
        }

        int x = -1;
        int y = 0;
        int num = 1;

        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                if (i % 3 == 0) { // 아래로 이동
                    x++;
                } else if (i % 3 == 1) { // 오른쪽으로 이동
                    y++;
                } else if (i % 3 == 2) { // 대각선으로 위로 이동
                    x--;
                    y--;
                }
                triangle[x][y] = num++;
            }
        }

        int index = 0;
        for (int[] row : triangle) {
            for (int val : row) {
                answer[index++] = val;
            }
        }

        


    
        return answer;
    }
}