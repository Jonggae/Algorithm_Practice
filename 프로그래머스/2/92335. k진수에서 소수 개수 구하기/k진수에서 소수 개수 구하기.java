import java.util.Arrays;
class Solution {
    public int solution(int n, int k) {
        int answer = 0;
        
        String num = convert(n,k);
        int cnt = 0;
        String[] nums = num.split("0");
        String[] nums2 = Arrays.stream(nums)
            .map(String::trim)
            .filter(s -> !s.isEmpty())
            .toArray(String[]::new);
          for (int i = 0; i <nums2.length ; i++) {
            boolean prime = checkPrime(Long.parseLong(nums2[i]));


            if (prime) {
                cnt++;
            }

        }
        answer = cnt;
        return answer;
    }
    
    static String convert(int n, int k) {
        StringBuilder sb = new StringBuilder();
        int temp = 0;
        temp = n;

        if (k == 10) {
            return String.valueOf(n);
        } else {
            while (temp>=k) {
                sb.append(temp % k);
                temp = temp / k;
            }
            sb.append(temp);
        }


        return String.valueOf(sb.reverse());
    }
    
     static boolean checkPrime(long p) {
        if(p <=1) return false;
        if(p ==2) return true;
        if(p %2 ==0) return false;

        long sqrt = (long) Math.sqrt(p);
        for (int i = 3; i <=sqrt ; i+=2) {
            if (p%i ==0) return false;
        }
        return true;
    }
}