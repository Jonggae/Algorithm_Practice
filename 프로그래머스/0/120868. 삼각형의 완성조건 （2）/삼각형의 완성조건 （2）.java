import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    public int solution(int[] sides) {
        int max = Arrays.stream(sides).sum();
        ArrayList<Integer> num = new ArrayList<>();
        if (sides[0] < sides[1]) {
            for (int i = 1; i < max; i++) {
                if(sides[1]-sides[0] < i && i < sides[0]+sides[1]){
                    num.add(i);
                }
            }
        }
        if (sides[0]> sides[1]) {
            for (int i = 1; i < max; i++) {
                if (sides[0] - sides[1] < i && i < sides[0] + sides[1]) {
                    num.add(i);
                }
            }
        }
        if( sides[0] == sides[1]) {
            for (int i = 1; i < max; i++) {
                if ( i < sides[0] + sides[1]) {
                    num.add(i);
                }
            }

        }
        int answer = num.size();
        return answer;
    }
}