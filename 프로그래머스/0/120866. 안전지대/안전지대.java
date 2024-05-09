class Solution {
    public int solution(int[][] board) {
        int answer = 0;
        int length = board.length;
        int[] di = {-1, -1, -1, 0, 0, 1, 1, 1};
        int[] dj = {-1, 0, 1, -1, 1, -1, 0, 1};
         for (int i = 0; i < length; i++) {
            for (int j = 0; j < length; j++) {
                if (board[i][j] == 0) {
                    boolean safe = true;
                    for (int k = 0; k < di.length; k++) {
                        int ni = i + di[k];
                        int nj = j + dj[k];

                        if (ni >= 0 & ni < length && nj >= 0 && nj < length) {
                            if (board[ni][nj] == 1) {
                                safe = false;
                                break;
                            }

                        }

                    }
                    if (safe) {
                        answer++;
                    }
                }

            }

        }
        
        
        return answer;
    }
}