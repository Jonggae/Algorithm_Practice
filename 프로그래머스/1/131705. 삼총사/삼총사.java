class Solution {
    public int solution(int[] number) {
        int answer = 0;
         int l = number.length;
        for (int i = 0; i <l ; i++) {
            for (int j = i+1; j <l ; j++) {
                for (int k = j+1; k <l ; k++) {
                    int trio = number[i]+number[j]+number[k];
                   if(trio==0) {
                       answer++;
                   }
               
            }            
            
        }

    }
        
        return answer;
    }
}