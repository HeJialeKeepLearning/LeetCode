package MedianofTwoSortedArrays;

public class Main {
    public static double findMedianSortedArrays(int[] nums1, int[] nums2) {

        int size=nums1.length+nums2.length;//合并后的数组大小
        int low=0,high=0;//low和high分别为计算中位数的两个数的下标

        if (size%2==0){//如果是偶数，取中间两个数的平均数
            high=size/2;
            low=high-1;
        }else {
            high=size/2;
            low=high;
        }

        double median=0.0;
        int[] nums=new int[size];

        int nums1Index=0,nums2Index=0,numIndex=0;
        while (nums1Index<nums1.length && nums2Index<nums2.length &&numIndex<=high){
            if (nums1[nums1Index]<nums2[nums2Index]){
                nums[numIndex]=nums1[nums1Index];
                nums1Index++;
            }else {
                nums[numIndex]=nums2[nums2Index];
                nums2Index++;
            }
            numIndex++;
        }

        if (numIndex==(high+1)){//如果是到了中位数的地方

        }else if (nums1Index==nums1.length){//如果nums1已经合并完了
            while (numIndex<=high){
                nums[numIndex]=nums2[nums2Index];
                nums2Index++;
                numIndex++;
            }
        }else if (nums2Index==nums2.length){//如果nums2已经合并完了
            while (numIndex<=high){
                nums[numIndex]=nums1[nums1Index];
                nums1Index++;
                numIndex++;
            }
        }

        median=(nums[low]+nums[high])/2.0;

        return median;

    }

    public static void main(String[] args){
        int[] nums1={1,3};
        int[] nums2={2};
        findMedianSortedArrays(nums1,nums2);
    }
}
