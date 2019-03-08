package ZigZagConversion;

public class main {
    static public String convert(String s, int numRows) {

        if (s.isEmpty()){
            return "";
        }

        if (numRows==1) return s;

        int T=numRows+(numRows-2);//周期大小
        int numCols=(s.length()/T+1)*(1+numRows-2);//Z型矩阵列数
        char[][] zMatrix=new char[numRows][numCols];

        for (int i=0;i<s.length();i++){
            int matrixRow=0;//Z型矩阵行
            int matrixCol=0;//Z型矩阵列

            int tNum=i/T;//在哪个周期中
            int tOffset=i%T;//在本周期的第几位

            //计算字符所在行、列
            if (tOffset>=numRows){//属于上升的部分
                matrixRow=numRows-1-(tOffset-numRows)-1;
                matrixCol=tNum*(1+(numRows-2))+tOffset-(numRows-1);
            }else {
                matrixRow=tOffset;
                matrixCol=tNum*(1+(numRows-2));
            }

            zMatrix[matrixRow][matrixCol]=s.charAt(i);
        }

        String resultStr="";
        for (int i=0;i<numRows;i++){
            for (int j=0;j<numCols;j++){
                if (zMatrix[i][j]!='\u0000'){
                    resultStr+=zMatrix[i][j];
                }
            }
        }

        return resultStr;
    }

    static public void main(String[] args){
        convert("PAYPALISHIRING",3);
    }
}
