class Solution {
    public int solution(int n) {
        int answer = 0;
        int times = 0;
        int contain = 0;
                int tempN = n;


        for (int i = 1; i < tempN + 1; i++) {
            if (i % 3 == 0) {
                tempN++;
                times++;
            }
            String num = String.valueOf(i);
            if (num.contains("3") && !(i % 3 == 0)) {
                tempN++;
                contain++;
            }
        }
        System.out.println(contain + times);
        answer = contain+times+n;
        return answer;
    }
}