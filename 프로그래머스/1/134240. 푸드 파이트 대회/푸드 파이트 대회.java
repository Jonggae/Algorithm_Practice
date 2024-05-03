class Solution {
    public String solution(int[] food) {
        String answer = "";
        StringBuilder sb = new StringBuilder();

        int water = food[0];
        String left ="";
        String right = "";

        for (int i = 1; i <food.length ; i++) {
            for (int j = 0; j <food[i]/2 ; j++) {
                left = String.valueOf(sb.append(i));
            }
        }

        right = String.valueOf(sb.reverse());
        answer = left+"0"+right;
        return answer;
    }
}