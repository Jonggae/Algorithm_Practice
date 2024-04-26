
import java.util.ArrayList;
class Solution {
    public int solution(int[] sides) {
        int answer = 0;
         int max = Math.max(sides[0],sides[1]);
        int min = Math.min(sides[0],sides[1]);
        ArrayList<Integer> num = new ArrayList<>();
        for (int i = 1; i <max+min ; i++) {
            if(max-min <i && i<max+min) {
                num.add(i);
            }

        }
        answer = num.size();
        return answer;
    }
}