import java.util.Arrays;
class Solution {
    public int solution(int[][] sizes) {
        int answer = 0;
        
         for (int i = 0; i < sizes.length; i++) {
            int l = sizes[i].length;
            for (int j = 0; j < l; j++) {
                if (sizes[i][j] < sizes[i][l - 1]) {
                    int temp = 0;
                    temp = sizes[i][j];
                    sizes[i][j] = sizes[i][l - 1];
                    sizes[i][l - 1] = temp;
                }
            }
        }
         int[] W = new int[sizes.length];
        int[] H = new int[sizes.length];

        for (int i = 0; i < sizes.length; i++) {
            for (int j = 0; j < sizes[i].length; j++) {
                if(j==0){
                    W[i] = sizes[i][0];
                } else {
                    H[i] = sizes[i][1];
                }

            }

        }
        int maxH = Arrays.stream(H).max().getAsInt();
        int maxW = Arrays.stream(W).max().getAsInt();

        answer = maxH * maxW;
        return answer;
    }
}