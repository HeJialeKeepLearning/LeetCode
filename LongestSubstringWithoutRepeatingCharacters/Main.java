package LongestSubstringWithoutRepeatingCharacters;

public class Main {
    public static int lengthOfLongestSubstring(String s) {

        int size=70000;

        int[] alphanumber=new int[size];
        for (int i=0;i<alphanumber.length;i++) alphanumber[i]=0;//数组初始化

        char a;
        int anumber;

        int p=0,pre=0;//用p表示队头，pre表示队尾
        int length=0;//记录不重复子串长度
        int lengthMax=length;//不重复子串长度的最大值

        while (p<s.length()){
            a=s.charAt(p);
            anumber=(int) a;
            alphanumber[anumber]++;//字母对应的数值增加，记录当前已有的字母
            while (alphanumber[anumber]>1){//元素依次出队，直到重复的元素不在队内
                char popAlpha=s.charAt(pre);
                int popNumber=(int) popAlpha;
                alphanumber[popNumber]--;
                pre++;
                length--;
            }
            p++;
            length++;
            lengthMax=lengthMax>length?lengthMax:length;//取变化中的max
        }

        return lengthMax;

    }

    public static void main(String[] args){

        lengthOfLongestSubstring("a bc");

    }
}
