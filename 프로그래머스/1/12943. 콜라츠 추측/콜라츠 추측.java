class Solution {
    public int solution(int num) {
        int answer = 0;
        
        long tempN = 0;
        int count = 0;
        tempN = num;
         while (tempN!=1) {
            if (tempN % 2 == 0) {
                tempN = tempN/2;
            }else {
                tempN = tempN*3+1;
            }
            count++;

            if (count>500) {
                count= -1;
                break;
            }

        }
        
        answer = count;
        
        return answer;
    }
}