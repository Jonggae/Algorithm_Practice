class Solution {
    public int solution(int storey) {
           int temp = 0;
        int cnt = 0;
        temp = storey;
        int answer = 0;
        
     while (temp != 0) {
            if (temp % 10 > 5) {
                cnt += 10 - (temp % 10);
                temp = (temp / 10) + 1;

            } else if (temp % 10 < 5) {
                cnt += temp % 10;
                temp = temp / 10;

            } else { // 자리수가 5일때
                if ((temp/10) %10 >=5) {
                    cnt += 10 - (temp % 10);
                    temp = (temp / 10) + 1;
            } else {
                    cnt += temp % 10;
                    temp = temp / 10;
                }
        }


    }
        
        answer = cnt;
        return answer;
    }
}