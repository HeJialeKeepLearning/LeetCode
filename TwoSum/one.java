package TwoSum;

public class one {
    public static int[] twoSum(int[] nums, int target) {
        int[] numsSorted=new int[nums.length];
        for (int i=0;i<nums.length;i++){
            numsSorted[i]=nums[i];
        }

        java.util.Arrays.sort(numsSorted);
        int i=0,j=numsSorted.length-1;
        int[] preresult=new int[2];
        while (i!=j){
            int sum=numsSorted[i]+numsSorted[j];
            if(sum==target){
                preresult[0]=numsSorted[i];
                preresult[1]=numsSorted[j];
                break;
            }else if (sum<target) i++;
            else j--;
        }

        int index=0;
        int[] result=new int[2];
        while (preresult[0]!=nums[index]){
            index++;
            if (index>=nums.length) break;
        }
        result[0]=index;
        index=nums.length-1;
        while (preresult[1]!=nums[index]){
            index--;
            if (index>=nums.length) break;
        }
        result[1]=index;

        return result;
    }

    public static void main(String[] args){
        int[] result=new int[2];
        int[] input={2,3,3,7};
        result=twoSum(input,6);
    }
}
