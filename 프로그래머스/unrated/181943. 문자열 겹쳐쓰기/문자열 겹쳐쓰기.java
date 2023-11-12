class Solution {
    public String solution(String my_string, String overwrite_string, int i) {
       
String pattern = my_string.substring(i,i+overwrite_string.length());   
        String answer1 = my_string.substring(0,i);
        String answer2 = my_string.substring(i,my_string.length());
        String answer3 = answer2.replace(pattern,overwrite_string);
        String answer = answer1 + answer3;
        return answer;
    }
}