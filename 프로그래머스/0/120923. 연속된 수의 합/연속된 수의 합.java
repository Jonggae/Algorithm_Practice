class Solution {
    public int[] solution(int num, int total) {
        int[] answer = new int[num];
          int a = 0;
        int temp = (2*total)/num;

        a= (temp-num+1)/2;

        

        for (int i = 0; i <num ; i++) {
            answer[i] = a+i;

        }
        
        return answer;
    }
}