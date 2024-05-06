import java.util.HashSet;
class Solution {
    public int solution(int[] nums) {
        int answer = 0;
         int pick = nums.length / 2;
        HashSet<Integer> pokemon = new HashSet<>();

        for (int i = 0; i < nums.length; i++) {
            pokemon.add(nums[i]);
        }

        
        answer = Math.min(pokemon.size(), pick);

        
        return answer;
    }
}