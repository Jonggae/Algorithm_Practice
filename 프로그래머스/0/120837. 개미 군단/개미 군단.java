class Solution {
    public int solution(int hp) {
        
        int ant = 0;
        int leftHp = 0;
if (hp > 5) {
            ant += hp / 5;
            leftHp = hp % 5; // 1 2 3 4 올 수 있음
            if (leftHp == 4 || leftHp==2) {
                ant += 2;
            }
            if (leftHp == 3 || leftHp==1) {
                ant++;
            }
        }else if(hp == 4 || hp==2) {
            ant = 2;
        }else if(hp == 3 || hp==1) {
            ant = 1;}
        int answer = ant;
        return answer;
    }
}