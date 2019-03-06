package LongestPalindromicSubstring;

public class Main {

    public static String longestPalindrome(String s) {

        int beginMax=0,endMax=0;//begin和end用于记录最长子串的位置
        int begin=0,end=0;//begin和end用于记录当前最长子串的位置

        for (int i=1;i<s.length()-1;i++){
            int ipre=i-1,inext=i+1;

            while (ipre>=0 && inext<s.length() && s.charAt(ipre)==s.charAt(inext)){
                ipre--;
                inext++;
            }

            if (ipre>=0 && inext<s.length()){//如果不对称
                begin=ipre+1;
                end=inext-1;
            }else if (ipre<0){//如果左边到头
                begin=0;
                if (inext>=s.length()){//如果右边到头
                    end=s.length()-1;
                }else end=inext-1;
            }


            if ((endMax-beginMax)<(end-begin)){//如果当前子串更长
                endMax=end;
                beginMax=begin;
            }
        }

        return s.substring(beginMax,endMax+1);

    }

    static public void main(String[] args){
        longestPalindrome("cbbd");
    }

}
