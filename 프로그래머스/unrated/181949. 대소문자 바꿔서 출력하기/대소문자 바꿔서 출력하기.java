import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        StringBuilder answer = new StringBuilder();
        
        for (int i=0; i<str.length(); i++) {
            if(str.charAt(i)==(str.toUpperCase().charAt(i))) {
                answer.append(str.toLowerCase().charAt(i));
            } else {
                answer.append(str.toUpperCase().charAt(i));
            }

        }
        System.out.println(answer);
    }
}