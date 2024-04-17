import java.util.HashSet;
class Solution {
    public int[] solution(int[] numbers) {
        HashSet<Integer> ans = new HashSet<>();
        int[] answer = {};
        int i= 0;
        int j= 0;
        
        for (i=0; i<numbers.length-1; i++) {
            for (j=i+1; j<numbers.length; j++) {
                int sum = numbers[i]+numbers[j];
                ans.add(sum);
                
            }
            
        }
        answer = ans.stream().sorted().mapToInt(Integer::intValue).toArray();
        return answer;
    }
}