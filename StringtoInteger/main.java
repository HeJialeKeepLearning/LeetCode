package StringtoInteger;

import java.math.BigInteger;

public class main {
    static public int myAtoi(String str) {

        str=str.trim();//去掉头尾空白字符
        if (str.isEmpty()) return 0;

        if (str.charAt(0)<'0' || str.charAt(0)>'9'){
            if (str.charAt(0)!='+' && str.charAt(0)!='-'){
                return 0;
            }
        }

        int end=0;
        if (str.charAt(0)=='-' || str.charAt(0)=='+'){
            end++;
        }

        while (end<str.length()){
            if (str.charAt(end)>='0' && str.charAt(end)<='9') end++;
            else break;
        }

        if ((str.charAt(0)=='-' && end==1) || end==0 || (str.charAt(0)=='+' && end==1)) return 0;

        BigInteger bigInteger=new BigInteger(str.substring(0,end));
        BigInteger intMax=new BigInteger(""+Integer.MAX_VALUE);
        BigInteger intMin=new BigInteger(""+Integer.MIN_VALUE);

        int resultMax=bigInteger.compareTo(intMax);
        int resultMin=bigInteger.compareTo(intMin);

        if (resultMax==1) return Integer.MAX_VALUE;
        if (resultMin==-1) return Integer.MIN_VALUE;

        return Integer.parseInt(str.substring(0,end));

    }

    static public void main(String[] args){
        myAtoi("+1");
    }
}
