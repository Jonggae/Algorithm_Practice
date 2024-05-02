import java.util.ArrayList;
import java.util.HashMap;

class Solution {
    public int solution(int left, int right) {
            HashMap<Integer, ArrayList<Integer>> div = new HashMap<>();
        ArrayList<Integer> divs;
        
        int answer = 0;
        
         for (int i = left; i <= right; i++) {
            ArrayList<Integer> temp = new ArrayList<>();
            for (int j = 1; j <= i; j++) {

                if (i % j == 0) {

                    temp.add(j);
                }

            }
            divs = temp;
            div.put(i,divs);
        }
         for (int i = left; i <=right ; i++) {
            if(div.get(i).size() % 2 == 0) {

                answer += i;
            }else {

                answer -= i;
            }

        }
        return answer;
    }
}