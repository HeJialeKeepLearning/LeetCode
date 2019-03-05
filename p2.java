import java.math.BigInteger;

public class p2 {

    public static class ListNode {
      int val;
      ListNode next;
      ListNode(int x) { val = x; }
    }

    public static ListNode addTwoNumbers(ListNode l1, ListNode l2){

        String str1=l1.val+"",str2=l2.val+"";
        ListNode p1=l1.next,p2=l2.next;
        while (p1!=null){
            str1+=p1.val;
            p1=p1.next;
        }
        while (p2!=null){
            str2+=p2.val;
            p2=p2.next;
        }

        String temp="";
        for (int i=str1.length()-1;i>=0;i--){
            temp+=""+str1.charAt(i);
        }
        str1=temp;

        temp="";
        for (int i=str2.length()-1;i>=0;i--){
            temp+=""+str2.charAt(i);
        }
        str2=temp;

        ListNode resulthead=new ListNode(0);
        ListNode resultp=resulthead;//尾指针


        try {
            int i1=0,i2=0,sum=0;
            i1=Integer.parseInt(str1.trim());
            i2=Integer.parseInt(str2.trim());
            sum=i1+i2;

            if (sum<0) throw new NumberFormatException();

            resulthead.val=sum%10;

            sum/=10;
            while (sum!=0){
                resultp.next=new ListNode(sum%10);
                sum/=10;
                resultp=resultp.next;
            }
        }catch (NumberFormatException e){

            BigInteger i1,i2,sum;
            i1=new BigInteger(str1.trim());
            i2=new BigInteger(str2.trim());
            sum=i1.add(i2);

            String bigSumStr=sum.mod(BigInteger.TEN).toString();
            int bigSumDigit=Integer.parseInt(bigSumStr);
            resulthead.val=bigSumDigit;

            sum=sum.divide(BigInteger.TEN);
            while (sum.compareTo(BigInteger.ZERO)>0){
                bigSumStr=sum.mod(BigInteger.TEN).toString();
                bigSumDigit=Integer.parseInt(bigSumStr);
                resultp.next=new ListNode(bigSumDigit);
                sum=sum.divide(BigInteger.TEN);
                resultp=resultp.next;
            }
        }

        return resulthead;


    }

    public static void main(String[] args){
        ListNode l1=new ListNode(31001);
        l1.next=new ListNode(90161);
        ListNode l2=new ListNode(558625);
        l2.next=new ListNode(8261);
        addTwoNumbers(l1,l2);

    }
}
