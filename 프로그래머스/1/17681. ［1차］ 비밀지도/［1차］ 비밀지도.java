class Solution {
    
    public String[] solution(int n, int[] arr1, int[] arr2) {
        
        
int[][] arr1Resolve = new int[n][n];
        int[][] arr2Resolve = new int[n][n];
        String[][] answerString = new String[n][n];
        String[] finalAnswer = new String[n];
        toDigit(arr1Resolve, arr1,n);
        toDigit(arr2Resolve, arr2,n);
        
         int[][] answer = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                answer[i][j] = arr1Resolve[i][j] + arr2Resolve[i][j];
            }

        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (answer[i][j] == 0) {
                    answerString[i][j] = " ";
                } else {
                    answerString[i][j] = "#";
                }
            }
        }
        for (int i = 0; i < n; i++) {
            StringBuilder sb = new StringBuilder();
            for (int j = 0; j < n; j++) {
                finalAnswer[i] = String.valueOf(sb.append(answerString[i][j]));
            }
        }
        
        return finalAnswer;
    }
    
      private static void toDigit(int[][] arr1Resolve, int[] arr1, int n) {
        for (int i = 0; i < arr1.length; i++) {
            int[] digit = new int[n];

            if (!(arr1[i] / 2 == 0)) {
                for (int j = digit.length - 1; j >= 0; j--) {
                    digit[j] = arr1[i] % 2;
                    arr1[i] = arr1[i] / 2;
                }
            }
            if (arr1[i] == 1) {
                digit[n - 1] = 1;
            }
            arr1Resolve[i] = digit;
        }
    }
    
    
}