class Solution {
    public int solution(String word) {
        int answer = 0;
          String vowel = "AEIOU";
        int[] state = {781, 156, 31, 6, 1};
        int num = 0;
        for (int i = 0; i < word.length(); i++) {

            num +=1+ vowel.indexOf(word.charAt(i)) * state[i];

        }
        answer = num;
        
        return answer;
    }
}