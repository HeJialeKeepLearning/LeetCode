package PalindromeNumber;

public class main {
    static public boolean isPalindrome(int x) {

        String xStr=""+x;

        if (xStr.length()==1) return true;

        int begin=0,end=xStr.length()-1;

        do {
            if (xStr.charAt(begin)==xStr.charAt(end)){
                begin++;
                end--;
            }
            else return false;
        }while (begin<end);

        return true;
    }

    static public void main(String[] args){
        isPalindrome(11);
    }
}
