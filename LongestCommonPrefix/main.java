package LongestCommonPrefix;

public class main {
    static public String longestCommonPrefix(String[] strs) {
        int size=strs.length;
        if (size==0) return "";
        char[] p=new char[size];
        int end=0;

        for (int i=0;i<size;i++){//初始化
            if (strs[i].length()==0) return "";
            p[i]=strs[i].charAt(0);
        }

        boolean flag=true;//flag=1表示前缀相同，flag=0表示不同

        //找到字符串数组中最短的字符串，记住下标index
        int index=0;
        for (int i=1;i<size;i++){
            if (strs[i].length()<strs[index].length()) index=i;
        }

        while (end<strs[index].length() && flag){//最长前缀不会超过最短字符串的长度

            for (int i=0;i<size-1;i++){
                if (strs[i].charAt(end)!=strs[i+1].charAt(end)){
                    flag=false;
                    break;
                }
            }

            if (flag) end++;
            else break;
        }

        return strs[0].substring(0,end);

    }

    static public void main(String[] args){
        String[] strs={"flower","flow","flight"};
        longestCommonPrefix(strs);
    }
}
