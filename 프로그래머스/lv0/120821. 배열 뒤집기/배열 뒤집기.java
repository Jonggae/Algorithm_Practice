class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = new int[num_list.length];
        int i= 0;
        for (i=0; i<num_list.length; i++){
        answer[i] = num_list[num_list.length-1-i];
        
            }
        return answer;
    }
}