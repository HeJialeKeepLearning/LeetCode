package ReverseInteger;

public class main {
    static public int reverse(int x) {
        String xStr="";
        String reverseStr="";
        boolean flag=true;//标示输入的整数是正还是负，true表示正数
        if (x<0){//如果x是负数
            x=-x;
            flag=false;
        }

        xStr=xStr+x;
        for (int i=xStr.length()-1;i>=0;i--){
            reverseStr+=xStr.charAt(i);
        }

        if (reverseStr.charAt(0)=='0'){//去掉头部的0
            if (reverseStr.length()>1)//如果不仅有0
                reverseStr=reverseStr.substring(1);
        }

        try {
            int resultInteger=Integer.parseInt(reverseStr);
        }catch (NumberFormatException e){
            return 0;
        }

        if (flag){
            return Integer.parseInt(reverseStr);
        }else return Integer.parseInt(reverseStr)*-1;
    }
}
