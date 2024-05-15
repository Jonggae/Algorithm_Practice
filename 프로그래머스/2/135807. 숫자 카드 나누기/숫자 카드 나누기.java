class Solution {
    public int solution(int[] arrayA, int[] arrayB) {
        int answer = 0;
         int gcdA = arrayA[0];
        int gcdB = arrayB[0];
        for (int i = 1; i < arrayA.length ; i++) {
            gcdA = gcd(gcdA,arrayA[i]);
            gcdB = gcd(gcdB,arrayB[i]);

        }

        boolean validA = true;
        boolean validB = true;
        for (int num : arrayB) {
            if (num % gcdA == 0) {
                validA = false;
                break;
            }

        }
        for (int num : arrayA) {
            if (num % gcdB == 0) {
                validB = false;
                break;
            }

        }

        if(validA) {
            answer = gcdA;
        }
        if(validB) {
            answer = Math.max(answer, gcdB);
        }
        return answer;
    }
      public static int gcd(int a, int b) {
        if (b == 0) return a;
        return gcd(b, a % b);
    }
}