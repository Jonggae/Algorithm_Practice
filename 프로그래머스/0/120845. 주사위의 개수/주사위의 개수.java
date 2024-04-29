class Solution {
    public int solution(int[] box, int n) {
        int answer = 0;
        int first = 1;
         for (int i = 0; i <box.length ; i++) {

            int temp = box[i]/n;
            first = first*temp;
        }
        answer = first;
        return answer;
    }
}